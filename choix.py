import tkinter as tk
from classes import *

def choisir_theme(theme):
    print(f"Thème choisi : {theme}")

def choisir_niveau(niveau):
    print(f"Niveau choisi : {niveau}")

def enregistrer_nom_joueur():
    nom_joueur = nom_joueur_entry.get()
    print(f"Nom du joueur enregistré : {nom_joueur}")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Jeu")

# Zone de saisie pour le nom du joueur
nom_joueur_label = tk.Label(fenetre, text="Nom du joueur:")
nom_joueur_label.pack()
nom_joueur_entry = tk.Entry(fenetre)
nom_joueur_entry.pack()

# Boutons pour les thèmes
theme1_button = tk.Button(fenetre, text="Thème 1", command=lambda: choisir_theme(1))
theme1_button.pack(side=tk.LEFT)
theme2_button = tk.Button(fenetre, text="Thème 2", command=lambda: choisir_theme(2))
theme2_button.pack(side=tk.LEFT)
theme3_button = tk.Button(fenetre, text="Thème 3", command=lambda: choisir_theme(3))
theme3_button.pack(side=tk.LEFT)

# Boutons pour les niveaux
niveau1_button = tk.Button(fenetre, text="Niveau 1", command=lambda: choisir_niveau(1))
niveau1_button.pack(side=tk.LEFT)
niveau2_button = tk.Button(fenetre, text="Niveau 2", command=lambda: choisir_niveau(2))
niveau2_button.pack(side=tk.LEFT)
niveau3_button = tk.Button(fenetre, text="Niveau 3", command=lambda: choisir_niveau(3))
niveau3_button.pack(side=tk.LEFT)

# Bouton pour enregistrer le nom du joueur
enregistrer_button = tk.Button(fenetre, text="Enregistrer", command=enregistrer_nom_joueur)
enregistrer_button.pack()

# Lancement de la boucle principale
fenetre.mainloop()