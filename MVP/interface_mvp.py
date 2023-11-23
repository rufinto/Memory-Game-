import tkinter as tk
from tkinter import Canvas
from tkinter import ttk
from cards_mvp import get_front_images
from cards_mvp import get_card_position
from classes_mvp import *
from PIL import Image, ImageTk

def create_window( title, color):
    window = tk.Tk()
    window.minsize(500,500)
    window.title(title)
    window.config(bg = color)
    return window

def create_label(window, t, f, b, fgg):
    title_label = tk.Label(window, text = t, font = f, bg = b, fg = fgg)
    title_label.pack(expand = "yes")

def create_frame(window, background, x, y, w, h):
    frame = tk.Frame(window, bg = background)
    frame.place(x=x, y=y, width=w, height=h)
    return frame
    
def create_grid(window, width, height, bg, rows, columns): #creee un canva avec une grille
    can = tk.Canvas(window, width = width, height = height, bg=bg)
    can.pack()
    can.grid(row = 0, column = 0, rowspan = rows, columnspan = columns)
    can.pack(expand='yes')
    return can

def add_button(frame, text, font, bg, fg, command):
    button = tk.Button(frame, text = text,font=font, bg=bg, fg=fg, command = command)
    button.pack()
    frame.pack(expand="Yes")
    return button

def open_playing_window_mvp(game, window, bg, front_images):
    rows = game.level.nb_row
    columns = game.level.nb_column
    line_height = 700//rows  #hauteur de chaque ligne
    column_width = 700//columns #largeur de chaque colonne
    
    card = Card.get_card_with_id(game.cards[0])
    back_image = Image.open(card.back)
    back_image = ImageTk.PhotoImage(back_image)
    
    playing_window = tk.Toplevel(window)
    
    playing_window.title("Game")
    playing_window.minsize(700,700)
    playing_window.config(bg = bg)
    
    can = create_grid(playing_window, 700, 700, bg, rows, columns)
    
    display_init_fronts_mvp(game = game, window=window, can = can, playing_window = playing_window, rows = rows, columns = columns, line_height = line_height, column_width = column_width, list = front_images, back_image = back_image )    
    
def display_init_fronts_mvp(game, window, can : Canvas, playing_window, rows, columns, line_height, column_width, list, back_image ): #list est la liste des images en format Image
    images_id = []
    for l in list :
        images_id.append(['']*len(l))
    for i in range(rows):
        for j in range(columns):
            images_id[i][j] = can.create_image(j*column_width + column_width/2 , i*line_height + line_height/2, image = list[i][j])
    for l in images_id: 
            for image_id in l : 
                can.itemconfig(image_id, image = back_image)
    can.bind("<Button-1>", lambda event : on_click_mvp(game , window, playing_window, event, can, images_id, list, line_height, column_width, back_image)) #"<Button-1>" : clic bouton gauche

def display_result_mvp(window, can, playing_window): #change la fenetre de jeu pour afficher game over or win 
    bg = '#C597FF'
    can.destroy()
    playing_window.minsize(500,500)
    frame = create_frame(playing_window, bg, 300, 400, 100, 200)
    create_label(playing_window, "WELL DONE ! YOU WON THIS GAME", ("Tahoma",20), bg, 'white' )
    add_button(frame, "QUIT", font=("Tahoma",20), bg=bg, fg='black', command = lambda : window.destroy())    

def on_click_mvp(game, window, playing_window, event, can, images_id, list, line_height, column_width, back_image):
    def get_clicked_image(event, line_height, column_width):
        x,y = event.x, event.y #coordonnes du click
        row = int(y)// line_height #ligne du click
        column = int(x)// column_width #colonne du click
        #verifier si le joueur a bien clique sur l'image ou bien sur un espace vide :
        center_x = column * column_width + column_width / 2
        center_y = row * line_height + line_height / 2
        if center_x - 113//2 <= x <= center_x + 113//2 and center_y - 170//2 <= y <= center_y + 170//2:
            return row, column
        else:
            return None, None

    i, j = get_clicked_image(event, line_height, column_width)
    if ( (i,j) != (None, None)):
        card_id = game.grid[i][j]
        card = Card.get_card_with_id(card_id)
        if not card.flipped and card.id not in game.flipped:  # Vérifie si la carte n'est pas déjà retournée et n'est pas déjà appariée
            card.flipped = True
            can.itemconfig(images_id[i][j], image=list[i][j])  # On affiche l'image
            game.flipped.append(card.id)
            if (len(game.flipped) % 2 == 0):
                previous_try_id = game.flipped[-2]
                previous_card = Card.get_card_with_id(previous_try_id)
                if card.is_pair_of(previous_card) == False:
                    can.after(1000, lambda: hide_unmatched_cards(game, can, images_id, card, previous_card, back_image))
                else :
                    game.matched_pairs += 1 #une paire en plus est trouvée                        
        if (game.is_finished()) :
            can.after(1000, lambda: display_result_mvp(window, can, playing_window))
        
def hide_unmatched_cards(game, can, images_id, card, previous_card, back_image):
    i, j = get_card_position(game, card.id)
    can.itemconfig(images_id[i][j], image=back_image)  # Retourne la carte actuelle

    k, l = get_card_position(game, previous_card.id)
    can.itemconfig(images_id[k][l], image=back_image)  # Retourne la carte précédente

    # Réinitialise les cartes dans la liste des cartes retournées
    card.flipped = False
    previous_card.flipped = False
    game.flipped.remove(card.id)
    game.flipped.remove(previous_card.id)

def display_main_game_interface_mvp(game):
    bg = '#C597FF'
    window = create_window("Memory Game", bg)
    frame = create_frame(window, bg, 400, 250, 5, 30)
    front_images = get_front_images(game)
    add_button(frame, "PLAY", font=("Tahoma",20), bg=bg, fg='black', command = lambda : open_playing_window_mvp(game, window, bg, front_images))
    window.mainloop()
