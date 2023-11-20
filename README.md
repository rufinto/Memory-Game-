# Memory Game with Tkinter

## Overview

This project is a group effort to create a memory game using Python and Tkinter for the graphical interface. The game is designed with object-oriented programming principles, follows test-driven development (TDD) practices, and features different themes such as cinema, monuments, student associations, and music.

## Requirements

- Python 3.11

## Installation

1. Clone the repository:

    ```bash
    git clone https://gitlab-research.centralesupelec.fr/sarra.ouhmidou/groupe12_memory
    ```

2. Change to the project directory:

    ```bash
    cd memory
    ```

3. Install dependencies:

    ```bash
    pip install pytest
    pip install tkinter
    ```

## Running the Game

To run the game, execute the following command in the project root directory:

```bash
python main.py



## Explication Utilité MVP

Le jeu doit se lancer avec le bon nombre de paires retournées et placées aléatoirement sur la grille. Au début du jeu, les cartes sont affichées pendant 5 secondes avant d'être cachées. Le joueur doit pouvoir sélectionner la carte qu'il veut retourner en cliquant dessus. Le joueur doit retourner deux cartes àa la suite, si les deux cartes constituent une paire (, un point est gagné,) les cartes restent retournées. Sinon, les deux cartes redeviennt cachées, le joueur ne gagne pas de point. Le jeu se termine lorsque toutes les cartes sont retournées.