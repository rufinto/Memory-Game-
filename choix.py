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

width = 500
height = 600

screen_x = fenetre.winfo_screenwidth()    
screen_y = fenetre.winfo_screenheight()
window_x = width
window_y = height

posX = (screen_x // 2) - (window_x // 2)
posY = (screen_y // 2) - (window_y // 2)
geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)

fenetre.minsize(width,height)
fenetre.title("Jeu")
fenetre.geometry(geo)

# Zone de saisie pour le nom du joueur
nom_joueur_label = tk.Label(fenetre, text="Nom du joueur:")
nom_joueur_label.grid(row=15, column=4)
nom_joueur_entry = tk.Entry(fenetre, width=50)
nom_joueur_entry.grid(row=25, column = 4)

# Boutons pour les thèmes
theme1_button = tk.Button(fenetre, text="Thème 1", command=lambda: choisir_theme(1))
theme1_button.grid(row = 100, column= 3)
theme2_button = tk.Button(fenetre, text="Thème 2", command=lambda: choisir_theme(2))
theme2_button.grid(row = 200, column = 3)
theme3_button = tk.Button(fenetre, text="Thème 3", command=lambda: choisir_theme(3))
theme3_button.grid(row = 300, column = 3)

# Boutons pour les niveaux
niveau1_button = tk.Button(fenetre, text="Niveau 1", command=lambda: choisir_niveau(1))
niveau1_button.grid(row= 100, column = 5)
niveau2_button = tk.Button(fenetre, text="Niveau 2", command=lambda: choisir_niveau(2))
niveau2_button.grid(row=200, column = 5)
niveau3_button = tk.Button(fenetre, text="Niveau 3", command=lambda: choisir_niveau(3))
niveau3_button.grid(row = 300, column = 5)

# Bouton pour enregistrer le nom du joueur
enregistrer_button = tk.Button(fenetre, text="Enregistrer", command=enregistrer_nom_joueur)
enregistrer_button.grid(row = 500, column = 4)

# Lancement de la boucle principale
fenetre.mainloop()