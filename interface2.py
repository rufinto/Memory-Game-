import tkinter as tk
from tkinter import Canvas
from classes import *
from cards import get_card_position
from cards import get_front_images
from PIL import Image, ImageTk
import time

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
    
def create_icanva(window, bg, w, h, x, y, image):
    can= tk.Canvas(window, width=w, height= h ,bg = bg,bd=0)
    can.place(x=x, y=y)
    can.create_image (w//2, h//2, image=image) #w//2 et h//2 sont la position de l'image dans le canva
    can.pack(expand='Yes')

def add_button(frame, text, font, bg, fg, command):
    button = tk.Button(frame, text = text,font=font, bg=bg, fg=fg, command = command)
    button.pack()
    frame.pack(expand="Yes")

def open_playing_window(game, window, bg, front_images):
    rows = game.level.nb_row
    columns = game.level.nb_column
    line_height = 700//rows  #hauteur de chaque ligne
    column_width = 700//columns #largeur de chaque colonne
    
    card = Card.get_card_with_id(game.cards[0])
    back_image = Image.open(card.back)
    back_image = ImageTk.PhotoImage(back_image)
    
    playing_window = tk.Toplevel(window)
    playing_window.title("Game")
    playing_window.minsize(800,700)
    playing_window.config(bg = bg)
    
    can = create_grid(playing_window, 700, 700, bg, rows, columns)
    display_init_fronts(game = game, can = can, playing_window = playing_window, rows = rows, columns = columns, line_height = line_height, column_width = column_width, list = front_images, back_image = back_image)    
    
def display_init_fronts(game, can : Canvas, playing_window, rows, columns, line_height, column_width, list, back_image): #list est la liste des images en format Image
    images_id = []
    for l in list :
        images_id.append(['']*len(l))
    for i in range(rows):
        for j in range(columns):
            images_id[i][j] = can.create_image(j*column_width + column_width/2 , i*line_height + line_height/2, image = list[i][j])
            
    countdown_label = tk.Label(playing_window, text="", font=("Helvetica", 30))
    countdown_label.pack(fill="both", expand=True)
    attempts_label = tk.Label(playing_window, text = "", font=("Helvetica", 30))
    attempts_label.pack(fill="both", expand=True)

    def display_result(result): #change la fenetre de jeu pour afficher game over or win 
        bg = '#C597FF'
        can.destroy()
        playing_window.minsize(500,500)
        if (result == 0):
            create_label(playing_window, "GAME OVER", ("Tahoma",20), bg, 'white' )
        if (result == 1):
            create_label(playing_window, "WELL DONE ! YOU WON THIS GAME", ("Tahoma",20), bg, 'white' )
        #playing_window.destroy()
        
    def update_init_countdown(seconds_left):
        countdown_label.config(text=str(seconds_left))
        if seconds_left > 0:
            playing_window.after(1000, lambda: update_init_countdown(seconds_left - 1)) #apres 1 seconde on rappele la fonction
        else:
            for list in images_id: 
                for image_id in list : 
                    can.itemconfig(image_id, image = back_image)
            game.started = True
            update_countdown(game.level.timer) #on lance le decompte pour la partie en fonction du niveau
     
    def update_countdown(seconds_left):
        countdown_label.config(text=str(seconds_left))
        if (seconds_left > 0 and game.is_finished() == (False, False)) :
            playing_window.after(1000, lambda: update_countdown(seconds_left - 1))
        elif (seconds_left <= 0 and game.is_finished() == (False, False)): #temps fini et tjrs pas trouve ttes les paires
            countdown_label.pack_forget() # on masque le label du chrono
            attempts_label.pack_forget()
            display_result(0) #0 : le joueur a perdu
        elif (seconds_left >0 and game.is_finished() == (False, True)) : #trop d'essais 
            countdown_label.pack_forget() # on masque le label du chrono
            attempts_label.pack_forget()
            display_result(0) #0 : le joueur a perdu
        elif (seconds_left >= 0 and game.is_finished() == (True, False)): #fini dans les temps et avec bon nombre d'essais
            countdown_label.pack_forget() # on masque le label du chrono
            attempts_label.pack_forget()
            display_result(1) #1 : le joueur a gagne
                        
    update_init_countdown(3) #on lance le decompte initiale
    can.bind("<Button-1>", lambda event : on_click(game, event, can, images_id, list, line_height, column_width, back_image, attempts_label )) #"<Button-1>" : clic bouton gauche
    display_attempts(game, attempts_label)

def display_attempts(game, attempts_label):
    attempts_label.config(text = game.attempts)
    
def on_click(game, event, can, images_id, list, line_height, column_width, back_image, attempts_label):
    
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

    if (game.started == True) : 
        i, j = get_clicked_image(event, line_height, column_width)
        if ( (i,j) != (None, None)):
            game.attempts += 1
            display_attempts(game, attempts_label)
            card_id = game.grid[i][j]
            card = Card.get_card_with_id(card_id)

            if not card.flipped and card.id not in game.flipped:  # Vérifie si la carte n'est pas déjà retournée et n'est pas déjà appariée
                card.flipped = True
                game.flipped.append(card.id)
                can.itemconfig(images_id[i][j], image=list[i][j])  # On affiche l'image

                if (len(game.flipped) % 2 == 0):
                    previous_try_id = game.flipped[-2]
                    previous_card = Card.get_card_with_id(previous_try_id)

                    if card.is_pair_of(previous_card) == False:
                        can.after(1000, lambda: hide_unmatched_cards(game, can, images_id, card, previous_card, back_image))
                    else :
                        game.matched_pairs += 1 #une paire en plus est trouvée 

def hide_unmatched_cards(game, can, images_id, card, previous_card, back_image):
    i, j = get_card_position(game, card)
    can.itemconfig(images_id[i][j], image=back_image)  # Retourne la carte actuelle

    k, l = get_card_position(game, previous_card)
    can.itemconfig(images_id[k][l], image=back_image)  # Retourne la carte précédente

    # Réinitialise les cartes dans la liste des cartes retournées
    card.flipped = False
    previous_card.flipped = False
    game.flipped.remove(card.id)
    game.flipped.remove(previous_card.id)

def create_grid(window, width, height, bg, rows, columns): #creee un canva avec une grille
    can = tk.Canvas(window, width = width, height = height, bg=bg)
    can.pack()
    can.grid(row = 0, column = 0, rowspan = rows, columnspan = columns)
    can.pack(expand='yes')
    return can

def display_main_game_interface(game):
    bg = '#C597FF'
    path = "3997691.png"
    window = create_window("Memory Game", bg)
    create_label (window,"MEMORY GAME", ("Tahoma",40), bg, 'white')
    image = Image.open(path)
    image = ImageTk.PhotoImage(image)
    create_icanva(window, bg, 250, 250, 250, 250, image)
    frame = create_frame(window, bg, 400, 250, 5, 30)
    front_images = get_front_images(game)
    add_button(frame, "PLAY", font=("Tahoma",20), bg=bg, fg='black', command = lambda : open_playing_window(game, window, bg, front_images))
    window.mainloop()