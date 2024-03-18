Évaluation de Demande de Prêt Immobilier

Ce projet utilise Python pour implémenter un service web composite pour l'évaluation des demandes de prêt immobilier. Il exploite diverses librairies pour gérer les services web SOAP, le logging, l'interaction avec le système, et la création de services web.

Utilisation de l'Environnement Virtuel
Ce projet utilise un environnement virtuel pour gérer les dépendances de manière isolée, assurant ainsi que le projet s'exécute dans un contexte défini et contrôlé. Suivez les instructions ci-dessous pour activer et utiliser l'environnement virtuel déjà configuré pour ce projet.

Activation de l'Environnement Virtuel
Avant de lancer ou de développer le projet, assurez-vous que l'environnement virtuel est activé. Voici comment procéder :

Sur Windows
Ouvrez une invite de commande ou PowerShell et naviguez jusqu'au répertoire du projet. Exécutez la commande suivante pour activer l'environnement virtuel :

.\env\Scripts\activate

Sur macOS et Linux
Ouvrez un terminal et naviguez jusqu'au répertoire du projet. Exécutez la commande suivante pour activer l'environnement virtuel :

source env/bin/activate

Installation des Dépendances
Si c'est la première fois que vous activez l'environnement virtuel ou si de nouvelles dépendances ont été ajoutées, installez les dépendances nécessaires à l'aide de pip :

pip install -r requirements.txt

Veillez à exécuter cette commande avec l'environnement virtuel activé pour garantir que les dépendances sont installées dans l'environnement virtuel et non dans votre environnement global Python.

Désactivation de l'Environnement Virtuel
Lorsque vous avez terminé de travailler dans l'environnement virtuel, vous pouvez le désactiver en exécutant :

deactivate

Cela vous ramènera à l'environnement global Python. Il est important de désactiver l'environnement virtuel lorsque vous avez terminé pour éviter toute confusion ou modification accidentelle des dépendances globales.

Assurez-vous d'ajuster les chemins et les noms de commandes en fonction de la configuration spécifique de votre projet;

AUTRE QUE L'ENVIRONNEMENT VIRTUEL

Prérequis

Python 3.x
pip (Gestionnaire de paquets Python)

Installation des Dépendances
Pour installer les dépendances nécessaires au projet, suivez les étapes ci-dessous. Ouvrez votre terminal ou invite de commande et assurez-vous que vous êtes dans le répertoire racine du projet.

Étape 1: Cloner le Répertoire (Optionnel)
Si le projet est hébergé sur un dépôt Git, commencez par le cloner :

git clone https://your-repository-url.git
cd your-project-name


Étape 2: Installer les Librairies Externes
Utilisez pip pour installer les librairies externes nécessaires :

Spyne pour la création de services web :

pip install spyne

Suds-jurko pour les interactions avec les services web SOAP. Notez que nous recommandons suds-jurko, une version maintenue du client SOAP suds original :

pip install suds-jurko

Étape 3: Vérification
Après l'installation, vous pouvez vérifier que les librairies sont correctement installées en utilisant la commande pip list, qui affichera toutes les librairies installées dans votre environnement.

Exécution de l'Application
Pour exécuter l'application, naviguez dans le répertoire du projet (si ce n'est pas déjà fait) et exécutez le script principal. Par exemple, si votre script principal est nommé app.py, utilisez la commande suivante :

python client.py
