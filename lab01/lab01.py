
TPS = 0.05
TVQ = 0.09975

def print_a_formatted_string():
    my_var = "World"
    my_number = 5
    my_string = "hello {}!\n my float number with 2 decimal is: {:.2f}".format(my_var, my_number)

    print(my_string)


def main():
    clients = lire_fichier('commandes.txt')

    imprimer_factures(clients)


def lire_fichier(fichier):
    clients = {}
    with open(fichier, 'r') as fichier_commande:
        for ligne in fichier_commande:
            ligne = ligne.split()
            ligne_commande = LigneCommande(ligne[1:])
            no_client = ligne[0]
            client = clients.get(no_client)

            if client:
                clients[no_client].ajouter_ligne_commande(ligne_commande)
            else:
                clients[no_client] = Commande(no_client)
                clients[no_client].ajouter_ligne_commande(ligne_commande)

    return clients


def imprimer_factures(clients):
    for client, commande in clients.items():
        with open('./factures/{}.txt'.format(client), 'w', encoding='utf8') as facture_client:
            facture_client.write('Client numéro {}\n\n'.format(client))
            facture_client.write('{:>27}{:>5}{:>10}{:>12}\n'.format('No de produit', 'Qte', 'Prix', 'Total (tx)'))

            for index, ligne in enumerate(commande.lignes_commande):
                facture_client.write('Produit #{:<5}{:<13}{:>5}{:>10.2f}{:>12.2f}\n'.format(index+1, ligne.no_produit, ligne.quantite, ligne.prix, ligne.calculer_total_taxe()))

            facture_client.write('\n')

            rabais = 0
            if commande.a_rabais():
                rabais = commande.total_commande * 0.15
                facture_client.write('Total avant rabais : {:.2f}\n'.format(commande.total_commande))
                facture_client.write('Rabais: {:.2f}\n'.format(rabais))

            facture_client.write('Total: {:.2f}\n'.format(commande.total_commande - rabais))


class Commande():
    def __init__(self, no_client):
        self.no_client = no_client
        self.lignes_commande = []
        self.rabais = False
        self.nombre_produit = 0
        self.total_commande = 0

    def ajouter_ligne_commande(self, ligne_commande):
        self.lignes_commande.append(ligne_commande)
        self.nombre_produit += ligne_commande.quantite
        self.total_commande += ligne_commande.calculer_total_taxe()

    def a_rabais(self):
        return self.nombre_produit >= 100


class LigneCommande():
    def __init__(self, ligne):
        self.no_produit = ligne[0]
        self.quantite = int(ligne[1])
        self.prix = float(ligne[2])
        self.taxe = ligne[3] if len(ligne) == 4 else None

    def calculer_total_taxe(self):
        total = self.calculer_total()

        if not self.taxe:
            total_taxe = 0
        elif "FP" in self.taxe:
            total_taxe = self.calculer_tps(total) + self.calculer_tvq(total)
        elif "F" in self.taxe:
            total_taxe = self.calculer_tps(total)
        else:
            total_taxe = self.calculer_tvq(total)

        return total + total_taxe

    def calculer_tps(self, total):
        return  TPS * total

    def calculer_tvq(self, total):
        return  TVQ * total

    def calculer_total(self):
        return self.quantite * self.prix


if __name__ == '__main__':
    main()