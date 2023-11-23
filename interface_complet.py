import tkinter as tk
from tkinter import Canvas
from tkinter import ttk
from PIL import Image, ImageTk

from classes import *

from cards import get_card_position
from cards import shuffle_cards

import time 

from interface_mvp import *

window_variables = []
#format : [window]
image_variables = []
#format : [front_images, images_id]
SHUFFLE = False
    
def create_icanva(window, bg, w, h, x, y, image):
    can= tk.Canvas(window, width=w, height= h ,bg = bg,bd=0)
    can.place(x=x, y=y)
    can.create_image (w//2, h//2, image=image) #w//2 et h//2 sont la position de l'image dans le canva
    can.pack(expand='Yes')


def open_playing_window(game, window, i_variables, bg, front_images, start):
    #detruire le bouton play :
    start.destroy()
    global image_variables
    image_variables = i_variables
    
    rows = game.level.nb_row
    columns = game.level.nb_column
    line_height = 700//rows  #hauteur de chaque ligne
    column_width = 700//columns #largeur de chaque colonne
    
    card = Card.get_card_with_id(game.cards[0])
    back_image = Image.open(card.back)
    back_image = ImageTk.PhotoImage(back_image)
    
    playing_window = tk.Toplevel(window)
    window_variables.append(playing_window)
    playing_window.title("Game")
    playing_window.minsize(700,700)
    playing_window.config(bg = bg)
    
    can = create_grid(playing_window, 700, 700, bg, rows, columns)
    
    attempts_label = tk.Label(playing_window, text="", font=("Helvetica", 20))
    window_variables.append(attempts_label)
    attempts_label.pack(fill = "both", expand=True)     
    countdown_label = tk.Label(playing_window, text="", font=("Helvetica", 20))
    countdown_label.pack(fill = "both", expand=True)
    
    display_init_fronts(game = game, can = can, playing_window = playing_window, rows = rows, columns = columns, line_height = line_height, column_width = column_width, list = front_images, back_image = back_image, countdown_label = countdown_label, attempts_label = attempts_label )    
    
def display_init_fronts(game, can : Canvas, playing_window, rows, columns, line_height, column_width, list, back_image, countdown_label, attempts_label  ): #list est la liste des images en format Image
    images_id = []
    for l in list :
        images_id.append(['']*len(l))
    for i in range(rows):
        for j in range(columns):
            images_id[i][j] = can.create_image(j*column_width + column_width/2 , i*line_height + line_height/2, image = list[i][j])
    
    image_variables.append(images_id)

    update_init_countdown(game, can, playing_window, countdown_label, attempts_label,  3, images_id, back_image) #on lance le decompte initiale
    can.bind("<Button-1>", lambda event : on_click(game, event, can, line_height, column_width, back_image, attempts_label, countdown_label, playing_window )) #"<Button-1>" : clic bouton gauche
    display_attempts(game, attempts_label)
    
def display_result(game, can, playing_window, result): #change la fenetre de jeu pour afficher game over or win 
    bg = '#C597FF'
    can.destroy()
    playing_window.minsize(500,500)
    frame = create_frame(playing_window, bg, 300, 400, 100, 200)
    if (result == 0):
        create_label(playing_window, "GAME OVER", ("Tahoma",20), bg, 'white' )
    if (result == 1):
        create_label(playing_window, "WELL DONE ! YOU WON THIS GAME", ("Tahoma",20), bg, 'white' )
    add_button(frame, "PLAY AGAIN", font=("Tahoma",20), bg=bg, fg='black', command = lambda : play_again(game, playing_window, can))
    add_button(frame, "QUIT", font=("Tahoma",20), bg=bg, fg='black', command = lambda : window_variables[0].destroy())    
    
def play_again(game, playing_window, can):
    can.destroy()
    playing_window.destroy()
    global SHUFFLE
    SHUFFLE = False
    for id in game.cards :
        card = Card.get_card_with_id(id)
        card.flipped = False
    for id in game.special_cards :
        card = Card.get_card_with_id(id)
        card.flipped = False
    
def update_init_countdown(game, can, playing_window, countdown_label, attempts_label, seconds_left, images_id, back_image):
    countdown_label.config(text=str(seconds_left))
    if seconds_left > 0:
        playing_window.after(1000, lambda: update_init_countdown(game, can, playing_window, countdown_label, attempts_label, seconds_left - 1, images_id, back_image)) #apres 1 seconde on rappele la fonction
    else:
        for list in images_id: 
            for image_id in list : 
                can.itemconfig(image_id, image = back_image)
        game.started = True
        update_countdown(game, can, playing_window, countdown_label, attempts_label, game.level.timer) #on lance le decompte pour la partie en fonction du niveau
     
def update_countdown(game, can, playing_window, countdown_label, attempts_label, seconds_left):
    if countdown_label.winfo_exists():  # Vérifie si le label existe encore
        countdown_label.config(text=str(seconds_left))
        if (seconds_left > 0 and game.is_finished() == (False, False)) :
            playing_window.after(1000, lambda: update_countdown(game, can, playing_window, countdown_label, attempts_label, seconds_left - 1))
        elif (seconds_left <= 0 and game.is_finished() == (False, False)): #temps fini et tjrs pas trouve ttes les paires
            countdown_label.pack_forget() # on masque le label du chrono
            attempts_label.pack_forget()
            display_result(game, can, playing_window, 0) #0 : le joueur a perdu
        elif (seconds_left >0 and game.is_finished() == (False, True)) : #trop d'essais 
            countdown_label.pack_forget() # on masque le label du chrono
            attempts_label.pack_forget()
            display_result(game, can, playing_window,0) #0 : le joueur a perdu
        elif (seconds_left >= 0 and game.is_finished() == (True, False)): #fini dans les temps et avec bon nombre d'essais
            countdown_label.pack_forget() # on masque le label du chrono
            attempts_label.pack_forget()
            display_result(game, can, playing_window, 1) #1 : le joueur a gagne

def display_attempts(game, attempts_label):
    attempts_label.config(text = game.level.max_attempts - game.attempts)

def special1_2(game, can, playing_window, countdown_label, attempts_label, i):
    
    def special2(playing_window, countdown_label): #retire 5s au chrono
        if countdown_label.winfo_exists():  # Vérifie si le label existe encore
            message_text = "Oups You lost 5 seconds...."    
            message_frame = tk.Frame(can, bd=5, relief=tk.SOLID)
            message_frame.place(relx=0.5, rely=0.5, anchor="center")
            message_element = tk.Label(message_frame, text=message_text, font=("Helvetica", 20), fg="black")
            message_element.pack(padx=10, pady=10) 
            playing_window.update()
            time.sleep(1)
            message_frame.destroy()   
        
            timer = int(countdown_label.cget("text"))
            countdown_label.destroy()
            countdown_label2 = tk.Label(playing_window, text="", font=("Helvetica", 20))
            countdown_label2.pack(fill = "both", expand = True)
            new_timer = timer - 5
            if (new_timer <= 0):
                return (countdown_label2, 0)      
            else :
                return (countdown_label2, new_timer)
        else :
            return None, None

    def special1(playing_window, countdown_label): #ajoute 10s au chrono
        if countdown_label.winfo_exists():  # Vérifie si le label existe encore
            
            message_text = "Youpii You won 10 seconds!!"    
            message_frame = tk.Frame(can, bd=5, relief=tk.SOLID)
            message_frame.place(relx=0.5, rely=0.5, anchor="center")
            message_element = tk.Label(message_frame, text=message_text, font=("Helvetica", 20), fg="black")
            message_element.pack(padx=10, pady=10) 
            playing_window.update()
            time.sleep(1)
            message_frame.destroy()            
            
            timer = int(countdown_label.cget("text"))
            countdown_label.destroy()
            countdown_label2 = tk.Label(playing_window, text="", font=("Helvetica", 20))
            countdown_label2.pack(fill = "both", expand = True)
            new_timer = timer + 10
            return (countdown_label2, new_timer)
        else :
            return None, None
        
    if (i == 1) :
        countdown_label, new_timer = special1(playing_window, countdown_label)
    elif (i == 2) :
        countdown_label, new_timer = special2(playing_window, countdown_label)
    if (countdown_label, new_timer) != (None, None) :
        update_countdown(game, can, playing_window, countdown_label, attempts_label, new_timer)
    return countdown_label

def special4(game, playing_window, can, front_images, back_image): #shuffle 
    new_grid = shuffle_cards(game) #change la grille du jeu 
    rows = game.level.nb_row
    columns = game.level.nb_column
    line_height = 700//rows  #hauteur de chaque ligne
    column_width = 700//columns #largeur de chaque colonne
    new_images_id = []
    new_front_images = []
    
    for l in new_grid :
        new_images_id.append([0]*len(l))
        new_front_images.append([0]*len(l))
        
    for i in range(rows):
        for j in range(columns):
            new_id = new_grid[i][j] #identifiant de la carte a mettre en position i,j
            k,l = get_card_position(game, new_id)
            new_front_images[i][j] = front_images[k][l]
            new_images_id[i][j] = can.create_image(j*column_width + column_width/2 , i*line_height + line_height/2, image = front_images[k][l])
                
    image_variables[0] = new_front_images
    image_variables[1] = new_images_id 
    
    game.grid = new_grid
    game.flipped = []
    game.matched_pairs = 0
    
    for i in range(rows):
        for j in range(columns):
            can.itemconfig(new_images_id[i][j], image = back_image)
            
    for id in game.cards :
        card = Card.get_card_with_id(id)
        card.flipped = False
        
    for id in game.special_cards :
        card = Card.get_card_with_id(id)
        card.flipped = False

    message_text = "The cards have been shuffeled...."
    message_frame = tk.Frame(can, bd=5, relief=tk.SOLID)
    message_frame.place(relx=0.5, rely=0.5, anchor="center")
    message_element = tk.Label(message_frame, text=message_text, font=("Helvetica", 20), fg="black")
    message_element.pack(padx=10, pady=10) 
    playing_window.update()
    time.sleep(1)
    message_frame.destroy()

def special3(game, playing_window, can, images_id, list):
    message_text = "A pair is revealed !!" 
    message_frame = tk.Frame(can, bd=5, relief=tk.SOLID)
    message_frame.place(relx=0.5, rely=0.5, anchor="center")
    message_element = tk.Label(message_frame, text=message_text, font=("Helvetica", 20), fg="black")
    message_element.pack(padx=10, pady=10) 
    playing_window.update()
    time.sleep(1)
    message_frame.destroy()       
    
    for (i,j) in Card.THEMES[game.theme] :
        if i in game.cards and i not in game.flipped:
            k,l = get_card_position(game, i)
            card1 = Card.get_card_with_id(i)
            card1.flipped = True
            can.itemconfig(images_id[k][l], image=list[k][l])
            m,n = get_card_position(game, j)
            card2 = Card.get_card_with_id(j)
            card2.flipped = True
            can.itemconfig(images_id[m][n], image=list[m][n])
            game.matched_pairs += 1
            game.flipped.append(i)
            game.flipped.append(j)
            return i,j

def on_click(game, event, can, line_height, column_width, back_image, attempts_label, countdown_label, playing_window):
    
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
        
    list = image_variables[0]
    images_id = image_variables[1]
    
    if (game.started == True) : 
        i, j = get_clicked_image(event, line_height, column_width)
        if ( (i,j) != (None, None)):
            game.attempts += 1
            display_attempts(game, attempts_label)
            card_id = game.grid[i][j]
            card = Card.get_card_with_id(card_id)
            if not card.flipped and card.id not in game.flipped:  # Vérifie si la carte n'est pas déjà retournée et n'est pas déjà appariée
                card.flipped = True
                can.itemconfig(images_id[i][j], image = list[i][j])  # On affiche l'image
                if (card.power == 0):
                    game.flipped.append(card.id) #on met pas les cartes speciales dans flipped à part la 3
                    if ((len(game.flipped) % 2 == 0 and 202 not in game.flipped)):
                        previous_try_id = game.flipped[-2]
                        previous_card = Card.get_card_with_id(previous_try_id)
                        if card.is_pair_of(previous_card) == False:
                            can.after(1000, lambda: hide_unmatched_cards(game, can, images_id, card, previous_card, back_image))
                        else :
                            game.matched_pairs += 1 #une paire en plus est trouvée                        
                    elif (202 in game.flipped and len(game.flipped) % 2 == 0) : #cas ou on avait deja une paire
                        game.flipped.remove(202) #on enleve la carte spe 3
                    elif (202 in game.flipped and (len(game.flipped) -1 ) % 2 == 0) : #cas ou on avait pas deja une paire
                        game.flipped.remove(202) #on enleve la carte spe 3
                        previous_try_id = game.flipped[-4] #on prend pas la paire ajoutée
                        previous_card = Card.get_card_with_id(previous_try_id)
                        if card.is_pair_of(previous_card) == False:
                            can.after(1000, lambda: hide_unmatched_cards(game, can, images_id, card, previous_card, back_image))
                        else :
                            game.matched_pairs += 1 #une paire en plus est trouvée
                else :
                    global SHUFFLE
                    if (card.power == 1):
                        special1_2(game, can, playing_window, countdown_label, attempts_label, 1)
                    elif (card.power == 2):
                        special1_2(game, can, playing_window, countdown_label, attempts_label, 2)
                    elif (card.power == 3):
                        game.flipped.append(card.id) 
                        special3(game, playing_window, can, images_id, list)
                    elif (card.power == 4 and SHUFFLE == False ):
                        SHUFFLE = True
                        special4(game, playing_window, can, list, back_image)
                        
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
