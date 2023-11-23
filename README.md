# Memory Game - Projet de Développement

Bienvenue dans le projet de développement collaboratif du jeu de mémoire en utilisant Python et Tkinter pour l'interface graphique. Ce projet est une initiative de groupe, conçu avec les principes de la programmation orientée objet, suit les pratiques du développement piloté par les tests (TDD), et propose différents thèmes tels que le cinéma, les monuments, les associations étudiantes de CS.

## Introduction
Le jeu Memory est une excellente façon d'exercer votre mémoire tout en vous amusant. Ce projet vise à créer une version améliorée du jeu Memory en utilisant Python et Tkinter pour l'interface graphique. Nous mettons l'accent sur la collaboration en groupe, en suivant les principes de la programmation orientée objet et en adoptant des pratiques de développement piloté par les tests (TDD).

## À Propos du Jeu Memory

Le jeu doit se lancer avec le bon nombre de paires retournées et placées aléatoirement sur la grille. Au début du jeu, les cartes sont affichées pendant 3 secondes avant d'être cachées. Le joueur doit pouvoir sélectionner la carte qu'il veut retourner en cliquant dessus. Le joueur doit retourner deux cartes à la suite, si les deux cartes constituent une paire les cartes restent retournées. Sinon, les deux cartes sont retournées. Il existe aussi dans la grille des cartes possédant des pouvoirs spéciaux utilisables une seule fois pendant une partie: 
- La carte "+10" ajoute dix secondes au chronomètre
- La carte "-5" enlève cinq secondes du chronomètre
- La carte "Shuffle" remélange aléatoirement les cartes
- La carte "Pair reveal" affiche une paire bonus. 
Aucune carte spéciale n'apparait dans le premier niveau.
Deux cartes spéciales apparaissent nécessairement dans les niveaux avancés.
Les cartes "+10" et "-5" n'apparaissent pas ensemble dans une meme partie.
Le jeu se termine soit quand le temps s'écoule, soit quand le joueur dépasse le nombre d'essais maximal permis ou bien lorsque toutes les cartes sont retournées.

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
- **Fonctionnalité 1 :** Création de toutes les classes nécessaires et les fonctions correspondantes: Card, Game et Level 
- **Fonctionnalité 2 :** sélection des thèmes et définition des pairs (dans un dictionnaire)
- **Fonctionnalité 3 :** initialiser la grille de cartes en choisissant une disposition initiale aléatoire  .

**Sprint 2 - Première interface graphique**
- **Fonctionnalité 4 :** création d’une première interface graphique avec le module Tkinter: fenêtre principale et une secondaire. 


**Sprint 3 - Gestion des actions du joueur**
- **Fonctionnalité 5 :** ajout de détection d’un click pour chaque carte qui permet d’afficher sa face.


- **Fonctionnalité 6 :** Tester les pairs et la fin du jeu.

**Sprint 4 - Jouer !**
- **Fonctionnalité 7 :** Mettre le jeu en marche.

### Objectif 2: Un Memory Game avec une meilleure interface graphique (Amélioration du MVP)

**Sprint 5 - Création de l'interface du jeu pour le choix des paramètres**
- **Fonctionnalité 8 :** Ajout d’un chronomètre pendant le jeu et d’un nombre d’essais maximal.

- **Fonctionnalité 9 :** Mise en place de deux fenêtres  permettant de choisir le thème et le niveau du jeu et d’une fenêtre permettant de relancer une partie ou fermer le jeu

### Objectif 3: Un Memory Game avec ajout de cartes spéciales.
- **Fonctionnalité 10:**  ajout de cartes spéciales qui apparaissent pendant une partie.
 
- **Fonctionnalité 11:** ajout des effets sonores pour dynamiser le jeu.


## Répartition des taches:
- Sarra Ouhmidou: F0, F1, F3, F5, F8, F10
- Maddie Bisch: F0, F2, F9
- Ghassen Znazen: F0, F3, F4, README, slides
- Myriam Boulaares: F0, F3, F9, F11, README
- Mathias Dunning--Laredo: F0, F6, tests unitaires
- Joan-Rufin Toukap: F0 ,F2, F6, F9





## Requirements

- Python 3.11

## Installation

1. Cloner :

    ```bash
    git clone https://gitlab-research.centralesupelec.fr/sarra.ouhmidou/groupe12_memory
    ```

2. Changer le dossier:

    ```bash
    cd groupe12_memory
    ```

3. Installer :

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
7. Une fois la partie est terminée vous pouvez soit quitter en cliquant sur "Quit" soit rejouer en cliquant sur "Play again".


Amusez-vous bien en jouant au jeu Memory!







