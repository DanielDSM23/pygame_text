# Projet pygame crée en 2021

Ce projet utilise la bibliothèque Pygame pour créer une application graphique permettant de visualiser des images et d'afficher du texte. De plus, il utilise le module Paho MQTT pour la communication avec un serveur MQTT.

## Installation des dépendances

Assurez-vous d'installer les bibliothèques nécessaires en exécutant la commande suivante :
```bash
pip install pygame paho-mqtt
```

## Utilisation

Exécutez le script principal `run.py` pour lancer l'application. Assurez-vous de remplacer l'adresse IP du broker MQTT dans le code si nécessaire.
````bash
python run.py
```
## Fonctionnalités

- **Gestion graphique :** Création d'une fenêtre graphique, gestion de l'affichage d'images et de texte.
- **Communication MQTT :** Utilisation du module Paho MQTT pour la communication avec un serveur MQTT.

## Remarques

- Le fichier `toolBox.py` contient des fonctions utilitaires.
- Le fichier `mqttFile.py` gère la communication MQTT.

N'hésitez pas à explorer et à personnaliser le code selon vos besoins.
