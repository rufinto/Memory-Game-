import tkinter as tk
from tkinter import Canvas
from classes import *
from cards import get_card_position
from cards import get_front_images
from PIL import Image, ImageTk
import pygame

# Initialisation de pygame pour la gestion du son
pygame.init()

# Chargement des sons
sound_first_page = pygame.mixer.Sound("sound_first_page.mp3")
sound_button_play = pygame.mixer.Sound("sound_button_play.mp3")
sound_wrong_pair = pygame.mixer.Sound("sound_wrong_pair.mp3")
sound_right_pair =pygame.mixer.Sound("sound_right_pair.mp3")

def play_sound(sound):
    pygame.mixer.Sound.play(sound)

def create_window(title, color, bg_image_path):
    window = tk.Tk()
    window.minsize(500, 500)
    window.title(title)
    
    # Set window background color    
    # Add background image
    if bg_image_path:
        bg_image = Image.open(bg_image_path)
        bg_image = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(window, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)
        bg_label.image = bg_image
    
    return window


def create_label(window, text, font, bg, fg):
    title_label = tk.Label(window, text=text, font=font, bg=bg, fg=fg)
    title_label.pack(expand="yes")
    return title_label  # Ajout de cette ligne pour retourner l'objet Label


def create_frame(window, background, x, y, w, h):
    frame = tk.Frame(window, bg=background)
    frame.place(x=x, y=y, width=w, height=h)
    return frame

def create_icanva(window, bg, w, h, x, y, image):
    can = tk.Canvas(window, width=w, height=h, bg=bg, bd=0)
    can.place(x=x, y=y)
    can.create_image(w//2, h//2, image=image)
    can.pack(expand='Yes')

def add_button(frame, text, font, bg, fg, command):
    button = tk.Button(frame, text=text, font=font, bg=bg, fg=fg, command=command)
    button.pack()
    

def open_playing_window(game, window,fond, front_images):
    # Jouer le son lors de l'ouverture de la fenêtre
    play_sound(sound_first_page)

    rows = game.level.nb_row
    columns = game.level.nb_column
    line_height = 500//rows
    column_width = 500//columns

    card = Card.get_card_with_id(game.cards[0])
    back_image = Image.open(card.back)
    back_image = ImageTk.PhotoImage(back_image)

    playing_window = tk.Toplevel(window)
    playing_window.title("Game")
    playing_window.minsize(500, 500)
    playing_window.config(bg=fond)

    can = create_grid(playing_window, 500, 500, fond, rows, columns)
    display_init_fronts(game=game, can=can, playing_window=playing_window, rows=rows, columns=columns, line_height=line_height, column_width=column_width, list=front_images, back_image=back_image)

def display_init_fronts(game, can: Canvas, playing_window, rows, columns, line_height, column_width, list, back_image):
    images_id = []
    for l in list:
        images_id.append([''] * len(l))
    for i in range(rows):
        for j in range(columns):
            images_id[i][j] = can.create_image(j*column_width + column_width/2, i*line_height + line_height/2, image=list[i][j])

    countdown_label = tk.Label(playing_window, text="", font=("Helvetica", 36))
    countdown_label.pack()

    def update_countdown(seconds_left):
        countdown_label.config(text=str(seconds_left))
        if seconds_left > 0:
            playing_window.after(1000, lambda: update_countdown(seconds_left - 1))
        else:
            countdown_label.pack_forget()
            for list in images_id:
                for image_id in list:
                    can.itemconfig(image_id, image=back_image)

    update_countdown(3)
    can.bind("<Button-1>", lambda event: on_click(game, event, can, images_id, list, line_height, column_width, back_image))

def on_click(game, event, can, images_id, list, line_height, column_width, back_image):

    def get_clicked_image(event, line_height, column_width):
        x, y = event.x, event.y
        row = int(y)//line_height
        column = int(x)//column_width
        return row, column

    i, j = get_clicked_image(event, line_height, column_width)
    if (i, j) == (None, None):
        return
    card_id = game.grid[i][j]
    card = Card.get_card_with_id(card_id)

    if not card.flipped and card.id not in game.flipped:
        card.flipped = True
        game.flipped.append(card.id)
        can.itemconfig(images_id[i][j], image=list[i][j])

        if (len(game.flipped) % 2 == 0):
            previous_try_id = game.flipped[-2]
            previous_card = Card.get_card_with_id(previous_try_id)

            if card.is_pair_of(previous_card) == False:
                play_sound(sound_wrong_pair)
                can.after(1000, lambda: hide_unmatched_cards(game, can, images_id, card, previous_card, back_image))
            else:
                game.matched_pairs += 1
                play_sound(sound_right_pair)

def hide_unmatched_cards(game, can, images_id, card, previous_card, back_image):
    i, j = get_card_position(game, card)
    can.itemconfig(images_id[i][j], image=back_image)

    k, l = get_card_position(game, previous_card)
    can.itemconfig(images_id[k][l], image=back_image)

    card.flipped = False
    previous_card.flipped = False
    game.flipped.remove(card.id)
    game.flipped.remove(previous_card.id)

def create_grid(window, width, height, bg, rows, columns):
    can = tk.Canvas(window, width=width, height=height, bg=bg)
    can.pack()
    can.grid(row=0, column=0, rowspan=rows, columnspan=columns)
    can.pack(expand='yes')
    return can

def display_main_game_interface(game):
    bg = 'mediumvioletred'
    window = create_window("Memory Game", color="black", bg_image_path="fond2.png")

    # Place "MEMORY GAME" label at the top center
    label_memory_game = create_label(window, "MEMORY GAME", ("Tahoma", 40), bg, 'white')
    label_memory_game.grid(row=0, column=0, columnspan=3, pady=(10, 0))

    # Create a frame for the button to achieve centering
    frame = create_frame(window, bg, 0, 0, 1, 1)
    frame.grid(row=1, column=0, pady=20)  # Center the frame

    front_images = get_front_images(game)
    add_button(frame, "PLAY", font=("Impact", 40), bg=bg, fg='white', command=lambda: open_playing_window(game, window, bg, front_images))
    window.mainloop()




# Appel de la fonction principale pour afficher l'interface du jeu
if __name__ == "__main__":
    # Vous pouvez ajouter ici le code pour ajouter du son lorsque le jeu est gagné
    game = YourGameClass()  # Remplacez YourGameClass() par votre classe de jeu réelle
    display_main_game_interface(game)
    

