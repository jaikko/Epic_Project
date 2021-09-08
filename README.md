# Epic_Project

**Description** 

Ce projet consiste à créer une API sécurisée RESTful en utilisant Django ORM

**Prérequis**

Il est nécessaire d'avoir Python 3.7, un IDE au choix(Viusal Studio Code par exemple), et Git installé sur le PC.

**Installation environnemnent virtuel**

1. Dans la console Git, choissisez l'emplacement où vous voulez cloner le projet
2. Exécuter  ``` https://github.com/jaikko/Epic_Project.git ```
3. Ensuite, se rendre dans le projet avec ``` cd Epic_Project ```
4. Installer l'environnement virtuel en éxécutant ``` python -m venv env ```
5. Activer le avec la commande   ``` source env/Scripts/activate ```
6. Installer les modules avec  ```pip install -r requirements.txt ```

**Configuration de la base de données**
1. Avec un IDE, ouvrir le projet
2. Dans le dossier P12, créer un fichier .env
3. Compléter ce fichier en respectant le format ci-dessous:  
 DATABASE_SECRET_KEY=  
 DATABASE_NAME=  
 DATABASE_USER=  
 DATABASE_PASS=  
 DATABASE_HOST=  
 DATABASE_PORT=
 
Pour plus d'information, consulter ce lien : https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f  
Pour générer un clé secrète, aller ici : https://djecrety.ir/
 
**Migration base de données**

Dans la racine du projet, exécuter ``` python manage.py makemigrations ``` puis ``` python manage.py migrate ```

**Création Admin**

1. Dans la console git, au niveau de la racine du projet, exécuter ``` winpty python manage.py createsuperuser ``` 
2. Renseigner un email et un mot de passe

**Lancement du server**

1. Dans la racine du projet, lancez le serveur avec la commande ```python manage.py runserver```

Pour accéder à site d'administration admin : http://127.0.0.1:8000/admin  
Pour connaître tous les points de terminaisons, consulter: https://documenter.getpostman.com/view/15210728/U16ev8Xz

**Rechercher et filtrer les informations**

Vous pouvez appliquer des filtres sur les terminaisons suivantes:

- */clients/?param="": first_name(string), last_name(string), email(string), phone(string), mobile(string), company_name(string)
- */contracts/?param="": status(boolean), amount_min(float) , amount_max(float) , amount_exact(float), payment_due_before(date), payment_due_after(date), payment_due_exact(date), client(email), sale_contact(email)
- */events/?param="": attendees_min(int) , attendees_max(int), attendees_exact(int), event_date_before(date), event_date_after(date), event_date_exact(date), client(email), event_status(string), support_contact(email)
- */status/?param="": status(string)

On peut utiliser plusieurs paramètres: */clients/?param=""&param=""  
Pour filter sur les dates, il faut utiliser le format suivant: Y-m-d
 

