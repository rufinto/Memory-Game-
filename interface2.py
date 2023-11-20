import tkinter as tk
from tkinter import Canvas
from classes import *
from cards import get_card_position
from cards import get_front_images
from PIL import Image, ImageTk
import time


def create_window(title, color):
    window = tk.Tk()
    window.minsize(500, 500)
    window.title(title)
    window.config(bg=color)
    return window


def create_label(window, t, f, b, fgg):
    title_label = tk.Label(window, text=t, font=f, bg=b, fg=fgg)
    title_label.pack(expand="yes")


def create_frame(window, background, x, y, w, h):
    frame = tk.Frame(window, bg=background)
    frame.place(x=x, y=y, width=w, height=h)
    return frame


def create_icanva(window, bg, w, h, x, y, image):
    can = tk.Canvas(window, width=w, height=h, bg=bg, bd=0)
    can.place(x=x, y=y)
    # w//2 et h//2 sont la position de l'image dans le canva
    can.create_image(w//2, h//2, image=image)
    can.pack(expand='Yes')


def add_button(frame, text, font, bg, fg, command):
    button = tk.Button(frame, text=text, font=font,
                       bg=bg, fg=fg, command=command)
    button.pack()
    frame.pack(expand="Yes")


def open_playing_window(game, window, bg, front_images):
    rows = game.level.nb_row
    columns = game.level.nb_column
    line_height = 700//rows  # hauteur de chaque ligne
    column_width = 700//columns  # largeur de chaque colonne

    card = Card.get_card_with_id(game.cards[0])
    back_image = Image.open(card.back)
    back_image = ImageTk.PhotoImage(back_image)

    playing_window = tk.Toplevel(window)
    playing_window.title("Game")
    playing_window.minsize(700, 700)
    playing_window.config(bg=bg)

    can = create_grid(playing_window, 700, 700, bg, rows, columns)
    display_init_fronts(game=game, can=can, playing_window=playing_window, rows=rows, columns=columns,
                        line_height=line_height, column_width=column_width, list=front_images, back_image=back_image)


# list est la liste des images en format Image
def display_init_fronts(game, can: Canvas, playing_window, rows, columns, line_height, column_width, list, back_image):
    images_id = []
    for l in list:
        images_id.append(['']*len(l))
    for i in range(rows):
        for j in range(columns):
            images_id[i][j] = can.create_image(
                j*column_width + column_width/2, i*line_height + line_height/2, image=list[i][j])

    countdown_label = tk.Label(playing_window, text="", font=("Helvetica", 30))
    countdown_label.pack(fill="both", expand=True)
    attempts_label = tk.Label(
        playing_window, text="attempts", font=("Helvetica", 30))
    attempts_label.pack(fill="both", expand=True)

    def display_result(result):
        bg = '#C597FF'
        can.destroy()
        playing_window.minsize(500, 500)
        game_over(result, playing_window)
        # playing_window.destroy()

    def update_init_countdown(seconds_left):
        countdown_label.config(text=str(seconds_left))
        if seconds_left > 0:
            playing_window.after(1000, lambda: update_init_countdown(
                seconds_left - 1))  # apres 1 seconde on rappele la fonction
        else:
            for list in images_id:
                for image_id in list:
                    can.itemconfig(image_id, image=back_image)
            game.started = True
            # on lance le decompte pour la partie en fonction du niveau
            update_countdown(game.level.timer)

    def update_countdown(seconds_left):
        countdown_label.config(text=str(seconds_left))
        if (seconds_left > 0 and game.is_finished() == (False, False)):
            playing_window.after(
                1000, lambda: update_countdown(seconds_left - 1))
        # temps fini et tjrs pas trouve ttes les paires
        elif (seconds_left <= 0 and game.is_finished() == (False, False)):
            countdown_label.pack_forget()  # on masque le label du chrono
            attempts_label.pack_forget()
            display_result(0)  # 0 : le joueur a perdu
        elif (seconds_left > 0 and game.is_finished() == (False, True)):  # trop d'essais
            countdown_label.pack_forget()  # on masque le label du chrono
            attempts_label.pack_forget()
            display_result(0)  # 0 : le joueur a perdu
        # fini dans les temps et avec bon nombre d'essais
        elif (seconds_left >= 0 and game.is_finished() == (True, False)):
            countdown_label.pack_forget()  # on masque le label du chrono
            attempts_label.pack_forget()
            display_result(1)  # 1 : le joueur a gagne

    update_init_countdown(3)  # on lance le decompte initiale
    can.bind("<Button-1>", lambda event: on_click(game, event, can, images_id, list, line_height,
             column_width, back_image, attempts_label))  # "<Button-1>" : clic bouton gauche


def on_click(game, event, can, images_id, list, line_height, column_width, back_image, attempts_label):

    def get_clicked_image(event, line_height, column_width):
        x, y = event.x, event.y  # coordonnes du click
        row = int(y) // line_height  # ligne du click
        column = int(x) // column_width  # colonne du click
        return row, column

    def display_attempts():
        attempts_label.config(text=game.attempts)

    display_attempts()
    if (game.started == True):
        i, j = get_clicked_image(event, line_height, column_width)
        if (i, j) == (None, None):
            return
        game.attempts += 1
        card_id = game.grid[i][j]
        card = Card.get_card_with_id(card_id)

        # Vérifie si la carte n'est pas déjà retournée et n'est pas déjà appariée
        if not card.flipped and card.id not in game.flipped:
            card.flipped = True
            game.flipped.append(card.id)
            # On affiche l'image
            can.itemconfig(images_id[i][j], image=list[i][j])

            if (len(game.flipped) % 2 == 0):
                previous_try_id = game.flipped[-2]
                previous_card = Card.get_card_with_id(previous_try_id)

                if card.is_pair_of(previous_card) == False:
                    can.after(1000, lambda: hide_unmatched_cards(
                        game, can, images_id, card, previous_card, back_image))
                else:
                    game.matched_pairs += 1  # une paire en plus est trouvée


def hide_unmatched_cards(game, can, images_id, card, previous_card, back_image):
    i, j = get_card_position(game, card)
    # Retourne la carte actuelle
    can.itemconfig(images_id[i][j], image=back_image)

    k, l = get_card_position(game, previous_card)
    # Retourne la carte précédente
    can.itemconfig(images_id[k][l], image=back_image)

    # Réinitialise les cartes dans la liste des cartes retournées
    card.flipped = False
    previous_card.flipped = False
    game.flipped.remove(card.id)
    game.flipped.remove(previous_card.id)


def create_grid(window, width, height, bg, rows, columns):  # creee un canva avec une grille
    can = tk.Canvas(window, width=width, height=height, bg=bg)
    can.pack()
    can.grid(row=0, column=0, rowspan=rows, columnspan=columns)
    can.pack(expand='yes')
    return can


def display_main_game_interface(game):
    bg = '#C597FF'
    path = "3997691.png"
    window = create_window("Memory Game", bg)
    create_label(window, "MEMORY GAME", ("Tahoma", 40), bg, 'white')
    image = Image.open(path)
    image = ImageTk.PhotoImage(image)
    create_icanva(window, bg, 250, 250, 250, 250, image)
    frame = create_frame(window, bg, 400, 250, 5, 30)
    front_images = get_front_images(game)
    add_button(frame, "PLAY", font=("Tahoma", 20), bg=bg, fg='black',
               command=lambda: open_playing_window(game, window, bg, front_images))
    window.mainloop()


def game_over(result: bool, fenetre):
    if result:
        image_path = "game_over_play_again.PNG"
    else:
        image_path = "game_over_play_again.PNG"

    def on_image_click(event):
        if event.x < 250:
            main()
        else:
            close_all_windows()

# Function to be called when the top part of the image is clicked
# Main function to create the Tkinter GUI

    def create_gui():
        # Create the main window
        # window = tk.Tk()
        # window.title("Game Over")

        # Load the image from the current directory
        image = Image.open(image_path)

        # Convert the image to Tkinter PhotoImage format
        tk_image = ImageTk.PhotoImage(image)

        # Create a canvas to display the image
        canvas = tk.Canvas(fenetre, width=500, height=500)
        canvas.pack()

        # Display the image on the canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

        # Bind click events on the canvas to the on_image_click function
        canvas.bind("<Button-1>", on_image_click)

        # Run the Tkinter main loop
        fenetre.mainloop()

    # Run the GUI
    create_gui()


def close_all_windows():
    for fen in window.winfo_children():
        if isinstance(fen, tk.Toplevel):
            fen.destroy()
