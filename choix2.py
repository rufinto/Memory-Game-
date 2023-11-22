import tkinter as tk

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
nom_joueur_label.pack(pady=10)
nom_joueur_entry = tk.Entry(fenetre)
nom_joueur_entry.pack(pady=10)

# Boutons pour les niveaux à gauche
niveau1_button = tk.Button(fenetre, text="Niveau 1", command=lambda: choisir_niveau(1), bg="lightblue", width=15, height=2)
niveau1_button.pack(side=tk.LEFT, padx=5)
niveau2_button = tk.Button(fenetre, text="Niveau 2", command=lambda: choisir_niveau(2), bg="lightgreen", width=15, height=2)
niveau2_button.pack(side=tk.LEFT, padx=5)
niveau3_button = tk.Button(fenetre, text="Niveau 3", command=lambda: choisir_niveau(3), bg="lightcoral", width=15, height=2)
niveau3_button.pack(side=tk.LEFT, padx=5)

# Bouton pour les thèmes à droite
theme_button = tk.Menubutton(fenetre, text="Choisir Thème", bg="orange", width=20, height=2)
theme_menu = tk.Menu(theme_button, tearoff=0)
theme_menu.add_command(label="Thème 1", command=lambda: choisir_theme(1))
theme_menu.add_command(label="Thème 2", command=lambda: choisir_theme(2))
theme_menu.add_command(label="Thème 3", command=lambda: choisir_theme(3))
theme_button['menu'] = theme_menu
theme_button.pack(side=tk.RIGHT, padx=5)

# Bouton pour enregistrer le nom du joueur
enregistrer_button = tk.Button(fenetre, text="Enregistrer", command=enregistrer_nom_joueur, bg="orange", width=20, height=2)
enregistrer_button.pack(pady=20)

# Lancement de la boucle principale
fenetre.mainloop()

