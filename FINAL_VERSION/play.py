from init_game_parameters import init_game
import tkinter as tk
from tkinter import Canvas
from tkinter import ttk
from PIL import Image, ImageTk

from interface_complet import *

from cards import get_front_images

OPTIONS = [0,0] #level, theme

def display_main_game_interface():
    if (len(window_variables) > 0):
        window_variables[0].destroy()
    bg = '#C597FF'
    path = "DATA/IMAGES/main_bg.png"
    window = create_window("Memory Game", bg)
    window_variables.append(window)
    create_label (window,"MEMORY GAME", ("Tahoma",40), bg, 'white')
    image = Image.open(path)
    image = ImageTk.PhotoImage(image)
    create_icanva(window, bg, 250, 250, 250, 250, image)
    frame = create_frame(window, bg, 400, 250, 5, 30)
    add_button(frame, "CHOOSE YOUR GAME OPTIONS", font=("Tahoma",20), bg=bg, fg='black', command = lambda : get_options(window))
    window.mainloop()

def get_options(window):
    options_window = tk.Toplevel(window)
    options_window.title("Options")
    options_window.minsize(600, 300)
    options_window.config(bg='#C597FF')

    opt_can = tk.Canvas(options_window, width=600, height=300, bg='#C597FF')
    opt_can.pack()

    image_theme1 = tk.PhotoImage(file="DATA/IMAGES/Theme1.png")
    image_theme2 = tk.PhotoImage(file="DATA/IMAGES/Theme2.png")
    image_theme3 = tk.PhotoImage(file="DATA/IMAGES/Theme3.png")

    opt_can.image_theme1 = image_theme1
    opt_can.image_theme2 = image_theme2
    opt_can.image_theme3 = image_theme3

    opt_can.create_image(100, 150, image=image_theme1)
    opt_can.create_text(100, 50, text="CS Associations", font=("Helvetica", 20), fill="black")

    opt_can.create_image(300, 150, image=image_theme2)
    opt_can.create_text(300, 50, text="Cinema", font=("Helvetica", 20), fill="black")

    opt_can.create_image(500, 150, image=image_theme3)
    opt_can.create_text(500, 50, text="Geography", font=("Helvetica", 20), fill="black")
    
    opt_can.bind("<Button-1>", lambda event: on_can_click(event))

    def on_can_click(event):
        x, y = event.x, event.y
        if 85 <= x <= 185 and 100 <= y <= 200:
            OPTIONS[1] = 1
            get_level()
        elif 215 <= x <= 385 and 100 <= y <= 200:
            OPTIONS[1] = 2
            get_level()
        elif 415 <= x <= 585 and 100 <= y <= 200:
            OPTIONS[1] = 3
            get_level()
    
    def get_level() :
        opt_can.destroy()
        level_var = tk.IntVar()
        level_label = tk.Label(options_window, text="Select Game Level", font=("Helvetica", 16), bg='#C597FF')
        level_label.pack()
        
        def on_level():
            OPTIONS[0] = level_var.get()        
        
        level_var.set(0)
        level_1 = tk.Radiobutton(options_window, text="4 pairs", variable=level_var, value=1, command=on_level, bg='#C597FF')
        level_1.pack()
        level_2 = tk.Radiobutton(options_window, text="8 pairs", variable=level_var, value=2, command=on_level, bg='#C597FF')
        level_2.pack()
        level_3 = tk.Radiobutton(options_window, text="10 pairs", variable=level_var, value=3, command=on_level, bg='#C597FF')
        level_3.pack()
        level_4 = tk.Radiobutton(options_window, text="12 pairs", variable=level_var, value=4, command=on_level, bg='#C597FF')
        level_4.pack()
        
        def validate():
            level = OPTIONS[0]
            theme = OPTIONS[1]
            game = init_game(level, theme)
            options_window.destroy()
            front_images = get_front_images(game)
            i_variables = []
            i_variables.append(front_images)
            frame = create_frame(window, '#C597FF', 400, 250, 5, 30)
            start = add_button(frame, "PLAY", font=("Tahoma",20), bg= '#C597FF', fg='black', command = lambda : open_playing_window(game, window, i_variables, '#C597FF', front_images, start))
        
        frame2 = create_frame(options_window, '#C597FF', 400, 250, 5, 30)
        add_button(frame2, "Validate", font=("Tahoma",20), bg='#C597FF', fg='black', command = validate)
