import tkinter as tk
from tkinter import ttk

def choisir_theme(theme):
    print(f"Thème choisi : {theme}")

def choisir_niveau(*args):
    print(f"Niveau choisi : {niveau_var.get()}")

def enregistrer_nom_joueur():
    nom_joueur = nom_joueur_entry.get()
    print(f"Nom du joueur enregistré : {nom_joueur}")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Jeu")
fenetre.geometry("700x700")  # Taille de la fenêtre
fenetre.configure(bg='#C597FF')  # Couleur de fond

# Zone de saisie pour le nom du joueur
nom_joueur_label = tk.Label(fenetre, text="Nom du joueur:", bg='#C597FF', font=("Arial", 16))
nom_joueur_label.pack(pady=20)
nom_joueur_entry = tk.Entry(fenetre, font=("Arial", 14))
nom_joueur_entry.pack(pady=10)

# Bouton pour les niveaux
niveaux_label = tk.Label(fenetre, text="Choisir Niveau:", bg='#C597FF', font=("Arial", 16))
niveaux_label.pack(pady=10)
niveaux_values = ["Niveau 1", "Niveau 2", "Niveau 3"]
niveau_var = tk.StringVar()
niveau_combobox = ttk.Combobox(fenetre, textvariable=niveau_var, values=niveaux_values, state="readonly", font=("Arial", 14))
niveau_combobox.pack(pady=10)
niveau_combobox.current(0)  # Sélectionner le premier niveau par défaut
niveau_combobox.bind("<<ComboboxSelected>>", choisir_niveau)

# Bouton pour les thèmes
themes_label = tk.Label(fenetre, text="Choisir Thème:", bg='#C597FF', font=("Arial", 16))
themes_label.pack(pady=10)
themes_values = ["Thème 1", "Thème 2", "Thème 3"]
theme_var = tk.StringVar()
theme_combobox = ttk.Combobox(fenetre, textvariable=theme_var, values=themes_values, state="readonly", font=("Arial", 14))
theme_combobox.pack(pady=10)
theme_combobox.current(0)  # Sélectionner le premier thème par défaut
theme_combobox.bind("<<ComboboxSelected>>", lambda event: choisir_theme(theme_var.get()))

# Bouton pour enregistrer le nom du joueur
enregistrer_button = tk.Button(fenetre, text="Enregistrer", command=enregistrer_nom_joueur, bg='#C597FF', font=("Arial", 16))
enregistrer_button.pack(pady=20)


# Lancement de la boucle principale
fenetre.mainloop()


