import tkinter as tk
from tkinter import Canvas, PhotoImage
from tkinter import ttk
import tkinter as tk
from tkinter import Canvas
from tkinter import ttk
from classes import *
from cards import get_card_position
from cards import get_front_images
from cards import shuffle_cards
from PIL import Image, ImageTk
from interface2 import create_window, display_main_game_interface
def choisir_theme(theme):
    print(f"Thème choisi : {theme}")

def choisir_niveau(*args):
    print(f"Niveau choisi : {niveau_var.get()}")

def enregistrer_nom_joueur():
    nom_joueur = nom_joueur_entry.get()
    print(f"Nom du joueur enregistré : {nom_joueur}")

def open_pseudo_window():
    def init_player():
        player = Player(pseudo.get())
        print(player.name)
        name.destroy()
        open_parameters_window()

    name = tk.Tk()
    name.minsize(600, 600)
    name.title('Choose a pseudo')

    # Ajouter une image de fond
    background_image = PhotoImage(file="fond1.png")  # Assurez-vous de mettre le bon chemin vers votre image
    background_canvas = Canvas(name, width=600, height=600)
    background_canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
    background_canvas.pack()

    name.config(bg='#C597FF')

    pseudo = tk.StringVar()
    tk.Label(name, text='Pseudo', font=("Tahoma", 20)).place(relx=0.2, rely=0.4, anchor=tk.CENTER)
    pseudo_entry = tk.Entry(name, textvariable=pseudo)
    pseudo_entry.place(relx=0.45, rely=0.4, anchor=tk.CENTER)

    tk.Button(name, text='Quit', command=name.quit, font=("Tahoma", 20)).place(relx=0.5, rely=0.85, anchor=tk.CENTER)
    tk.Button(name, text='Confirm', command=init_player, font=("Tahoma", 20)).place(relx=0.8, rely=0.4, anchor=tk.CENTER)

    name.mainloop()

def open_parameters_window():
    level_window = create_window('Choose difficulty', '#C597FF')
    id_level_var = tk.IntVar()

    def ShowChoice():
        level_window.destroy()
        if id_level_var.get() == 1:
            level = Level(id=1, nb_pairs=4, nb_row=2, nb_column=4)
        elif id_level_var.get() == 2:
            level = Level(id=2, nb_pairs=7, nb_row=4, nb_column=4)
        elif id_level_var.get() == 3:
            level = Level(id=3, nb_pairs=9, nb_row=4, nb_column=5)
        elif id_level_var.get() == 4:
            level = Level(id=4, nb_pairs=10, nb_row=4, nb_column=6)

        def init_globale():
            theme = theme_var.get()
            game = Game(level, theme)
            theme_window.destroy()
            display_main_game_interface(game)

        theme_window = create_window('Select a theme', '#C597FF')
        theme_var = tk.IntVar()
        tk.Label(theme_window, text='Select theme', font=("Tahoma", 20)).place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        tk.Radiobutton(theme_window, text="assos CS", value=1, variable=theme_var, command=init_globale,
                       font=("Tahoma", 20)).place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        tk.Radiobutton(theme_window, text="duos iconiques", value=2, variable=theme_var, command=init_globale,
                       font=("Tahoma", 20)).place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        tk.Radiobutton(theme_window, text="géographie des monuments", value=3, variable=theme_var, command=init_globale,
                       font=("Tahoma", 20)).place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    tk.Label(level_window, text='Select difficulty', font=("Tahoma", 20)).place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    tk.Radiobutton(level_window, text="4 paires", value=1, variable=id_level_var, command=ShowChoice,
                   font=("Tahoma", 20)).place(relx=0.25, rely=0.45, anchor=tk.CENTER)
    tk.Radiobutton(level_window, text="8 paires", value=2, variable=id_level_var, command=ShowChoice,
                   font=("Tahoma", 20)).place(relx=0.25, rely=0.7, anchor=tk.CENTER)
    tk.Radiobutton(level_window, text="10 paires", value=3, variable=id_level_var, command=ShowChoice,
                   font=("Tahoma", 20)).place(relx=0.75, rely=0.45, anchor=tk.CENTER)
    tk.Radiobutton(level_window, text="12 paires", value=4, variable=id_level_var, command=ShowChoice,
                   font=("Tahoma", 20)).place(relx=0.75, rely=0.7, anchor=tk.CENTER)
    tk.mainloop()

# Exemple d'utilisation
open_pseudo_window()
