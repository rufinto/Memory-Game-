# Memory Game - Projet de Développement

Bienvenue dans le projet de développement collaboratif du jeu de mémoire en utilisant Python et Tkinter pour l'interface graphique. Ce projet est une initiative de groupe, conçu avec les principes de la programmation orientée objet, suit les pratiques du développement piloté par les tests (TDD), et propose différents thèmes tels que le cinéma, les monuments, les associations étudiantes de CS.

## Introduction
Le jeu Memory est une excellente façon d'exercer votre mémoire tout en vous amusant. Ce projet vise à créer une version améliorée du jeu Memory en utilisant Python et Tkinter pour l'interface graphique. Nous mettons l'accent sur la collaboration en groupe, en suivant les principes de la programmation orientée objet et en adoptant des pratiques de développement piloté par les tests (TDD).

## À Propos du Jeu Memory

Le jeu doit se lancer avec le bon nombre de paires retournées et placées aléatoirement sur la grille. Au début du jeu, les cartes sont affichées pendant 5 secondes avant d'être cachées. Le joueur doit pouvoir sélectionner la carte qu'il veut retourner en cliquant dessus. Le joueur doit retourner deux cartes à la suite, si les deux cartes constituent une paire (un point est gagné) les cartes restent retournées. Sinon, les deux cartes redeviennt cachées, le joueur ne gagne pas de point. Le jeu se termine lorsque toutes les cartes sont retournées.

## Organisation du Projet

### Structure du projet (main)
- MVP: ce dossier contient les classes et les packages nécessaires au lancement du jeu à travers le fichier main_mvp_launch.py. Il contient aussi les différentes images dans un dossier nommé DATA_MVP.
- FINAL_VERSION: ce dossier contient les classes et les packages nécessaires au lancement du jeu à travers le fichier main_final_launch.py. Il contient aussi les différentes images et les sons dans un dossier nommé DATA.

### Objectif 1 (MVP): Un jeu Memory Minimum

**Sprint 0 - Analyse du problème et réflexion autour de la conception**
Le jeu doit permettre au joueur de:
- Générer aléatoirement les cartes de la grille de jeu.
- Jouer en lui demandant de choisir deux cartes et de vérifier qu’ils appartiennent au même couple.
- Tester la fin du jeu .

**Sprint 1 - Mise en Place des Données du Jeu**
- **Fonctionnalité 1 :** Création de toutes les classes nécessaires et les fonctions correspondantes: Card, Game et Player 
- **Fonctionnalité 2 :** initialiser la grille de cartes en choisissant une disposition initiale aléatoire  .

**Sprint 2 - Première interface graphique**
- **Fonctionnalité 3 :** création d’une première interface graphique avec le module Tkinter.

**Sprint 3 - Gestion des actions du joueur**
- **Fonctionnalité 4 :** ajout de boutons pour chaque carte qui permet d’afficher sa face pendant une courte durée 

- **Fonctionnalité 5 :** Gestion des retournements et tester la fin du jeu.

**Sprint 4 - Jouer !**
- **Fonctionnalité 6 :** Mettre le jeu en marche.

### Objectif 2: Un Memory Game avec une meilleure interface graphique (Amélioration du MVP)

**Sprint 5 - Création de l'interface pour la grille de jeu**
- **Fonctionnalité 7 :** Mise en place d’une fenêtre principale permettant de choisir le thème et le niveau du jeu et d’une fenêtre permettant de relancer une partie ou fermer le jeu.
- **Fonctionnalité 6 :** Ajout d’un chronomètre pendant le jeu et de messages.

### Objectif 3: Un Memory Game avec la gestion des joueurs, de leur score et ajout de cartes spéciales.
- Le jeu dispose de nouvelles fonctions spéciales notamment le calcul du score du joueur et l'ajout de cartes spéciales qui apparaissent pendant le jeu. En plus, des musiques de fond ont été ajoutés pour rendre le jeu plus agréable





## Requirements

- Python 3.11

## Installation

1. Clone the repository:

    ```bash
    git clone https://gitlab-research.centralesupelec.fr/sarra.ouhmidou/groupe12_memory
    ```

2. Change to the project directory:

    ```bash
    cd groupe12_memory
    ```

3. Install dependencies:

    ```bash
    pip install pytest
    pip install tkinter
    pip install pillow
    pip install pygame
    ```

## Comment lancer le MVP
1. Positionnez vous sur la branche main.
2. Ouvrir le dossier MVP
3. Exécuter le fichier main_mvp_launch.py


## Comment Jouer le jeu final

1. Ouvrir le dossier FINAL_VERSION 
2. Lancer le jeu en exécutant le fichier main_final_launch.py
3. Choisir les paramètres du jeu (niveau et thème)
4. Observez les cartes et essayez de trouver des paires identiques.
5. Cliquez sur deux cartes pour les retourner. Si elles sont identiques, elles resteront visibles.
6. Continuez à tourner les cartes jusqu'à ce que toutes les paires soient trouvées. Faites attention au chronomètre et au nombre d'essais maximal.



Amusez-vous bien en jouant au jeu Memory!







