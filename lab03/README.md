# Lab03

Piste de solution du laboratoire 3 dans le cadre du cours [INF3005](http://jberger.org/inf3005/) enseigné par Jacques Berger.

## 1. Installer Flask
```
pip3 install Flask

# si sur les ordinateurs de l'UQAM:
pip3 install --user flask
```

## 2. Créer l'application Flask de base en créant un fichier nommé `my_app.py` et y mettre le contenu suivant:

```
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
```

## 3. Créer un dossier appelé `templates` et y ajouter `index.html` contenant le code suivant:

```
<html>
    <head>
        <title>Index</title>
        <meta charset='utf-8'>
    </head>
    <body>
        <h1>Index</h1>
        <p>Here is my first page.</p>
    </body>
</html>
```

## 4. Définir les variables d'environnements d'un shell à l'aide d'un `makefile`

```
# Indiquer à flask quel est la racine de l'application à rouler.
export FLASK_APP=my_app.py
# Indiquer à flask que nous sommes en mode debug/developpement
# Permet le refresh du serveur automatiquement lors de changement dans le code et l'affichage des erreurs
export FLASK_DEBUG=1

run:
    flask run
```

## 5. Ajouter un fichier vide nommé `__init__.py`

## 6. Lancer le `makefile` et aller voir dans le fureteur à l'adresse Indiquée lors du lancement du serveur.

### 7. Apporter les modifications à `index.html` pour avoir un formulaire.

### 8. Apporter les modifications à `my_app.py` pour attraper l'information du formulaire.

- Importez `request` pour obtenir les informations du formulaire et `redirect` pour rediriger le client vers une autre route.

- Assurez vous de créer un template pour la route a rediriger.

```
valeur_du_champ = request.form['nom_champ']
return redirect('nom_route_a_rediriger')
```
