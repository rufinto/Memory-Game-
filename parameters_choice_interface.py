import tkinter as tk
from tkinter import Canvas
from tkinter import ttk
from classes import *
from cards import get_card_position
from cards import get_front_images
from cards import shuffle_cards
from PIL import Image, ImageTk
from interface2 import *

def open_pseudo_window():
    def init_player():
        player = Player(player_name)
        name.destroy()
        open_parameters_window()
    name = create_window('Saisissez votre pseudo joueur','#C597FF')
    tk.Label(name,text = 'Name').grid(row = 0)
    player_name = tk.Entry(name)
    player_name.grid(row = 0, column = 1)
    tk.Button(name, text = 'Quit', command = name.quit).grid(row = 3, column = 0, sticky = tk.W, pady = 4)
    tk.Button(name, text = 'Confirm', command=init_player).grid(row = 3, column = 1, sticky = tk.W, pady = 4)
    name.mainloop()

def open_parameters_window(): 
    level_window = create_window('Choose difficulty', '#C597FF')
    id_level_var = tk.IntVar()
    def ShowChoice():
        level_window.destroy()
        if id_level_var.get() == 1:
            level = Level(id = 1, nb_pairs = 4, nb_row = 2, nb_column = 4)
        elif id_level_var.get() == 2:
            level = Level(id = 2, nb_pairs = 7, nb_row = 4, nb_column = 4)
        elif id_level_var.get() == 3:
            level = Level(id = 3, nb_pairs = 9, nb_row = 4, nb_column = 5)
        elif id_level_var.get() == 4:
            level = Level(id = 4, nb_pairs = 10, nb_row = 4, nb_column = 6)
        def init_globale():
            theme = theme_var.get()
            game = Game(level,theme)
            theme_window.destroy()
            display_main_game_interface(game)
        theme_window = create_window('Select a theme','#C597FF')
        theme_var = tk.IntVar()
        tk.Label(theme_window, text = 'Select theme', justify = tk.LEFT).pack()
        tk.Radiobutton(theme_window,text = "assos CS",value=1,variable=theme_var,command=init_globale).pack(anchor=tk.W)
        tk.Radiobutton(theme_window,text = "duos iconiques",value=2,variable=theme_var,command=init_globale).pack(anchor=tk.W)
        tk.Radiobutton(theme_window,text = "géographie des monuments",value=3,variable=theme_var,command=init_globale).pack(anchor=tk.W)
    tk.Label(level_window, text = 'Select difficulty', justify = tk.LEFT).pack()
    tk.Radiobutton(level_window,text = "4 paires",value=1,variable=id_level_var,command=ShowChoice).pack()
    tk.Radiobutton(level_window,text = "8 paires",value=2,variable=id_level_var,command=ShowChoice).pack()
    tk.Radiobutton(level_window,text = "10 paires",value=3,variable=id_level_var,command=ShowChoice).pack()
    tk.Radiobutton(level_window,text = "12 paires",value=4,variable=id_level_var,command=ShowChoice).pack()
    tk.mainloop()