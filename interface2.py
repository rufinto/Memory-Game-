import tkinter as tk
from tkinter import Canvas
from tkinter import ttk
from classes import *
from cards import get_card_position
from cards import get_front_images
from cards import shuffle_cards
from PIL import Image, ImageTk

def create_window(title, color):
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
    button = tk.Button(frame, text = text,font = font, bg = bg, fg = fg, command = command)
    button.pack()
    frame.pack(expand="Yes")

def open_pseudo_window():
    def init_player():
        player = Player(player_name)
        name.destroy()
    name = create_window('Saisissez votre pseudo joueur','light blue')
    tk.Label(name,text = 'Name').grid(row = 0)
    player_name = tk.Entry(name)
    player_name.grid(row = 0, column = 1)
    tk.Button(name, text = 'Quit', command = name.quit).grid(row = 3, column = 0, sticky = tk.W, pady = 4)
    tk.Button(name, text = 'Confirm', command=init_player).grid(row = 3, column = 1, sticky = tk.W, pady = 4)
    name.mainloop()

def open_parameters_window(): 
    level_window = create_window('Choose difficulty', 'light blue')
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
            return(game)
        theme_window = create_window('Select a theme','light blue')
        theme_var = tk.IntVar()
        tk.Label(theme_window, text = 'Select theme', justify = tk.LEFT).pack()
        tk.Radiobutton(theme_window,text = "assos CS",value=1,variable=theme_var,command=init_globale).pack(anchor=tk.W)
        tk.Radiobutton(theme_window,text = "duos iconiques",value=2,variable=theme_var,command=init_globale).pack(anchor=tk.W)
        tk.Radiobutton(theme_window,text = "géographie des monuments",value=3,variable=theme_var,command=init_globale).pack(anchor=tk.W)
    tk.Label(level_window, text = 'Select difficulty', justify = tk.LEFT).pack()
    tk.Radiobutton(level_window,text = "4 paires",value=1,variable=id_level_var,command=ShowChoice).pack()
    tk.Radiobutton(level_window,text = "8 paires",value=2,variable=id_level_var,command=ShowChoice).pack()
    tk.Radiobutton(level_window,text = "10 paires",value=3,variable=id_level_var,command=ShowChoice).pack()
    tk.Radiobutton(level_window,text = "10 paires",value=4,variable=id_level_var,command=ShowChoice).pack()
    tk.mainloop()

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
    playing_window.minsize(700,700)
    playing_window.config(bg = bg)
    
    can = create_grid(playing_window, 700, 700, bg, rows, columns)
    display_init_fronts(game = game, can = can, playing_window = playing_window, rows = rows, columns = columns, line_height = line_height, column_width = column_width, list = front_images, back_image = back_image)    
    
def display_init_fronts(game, can : Canvas, playing_window, rows, columns, line_height, column_width, list, back_image, init_time = 3): #list est la liste des images en format Image
    images_id = []
    for l in list :
        images_id.append(['']*len(l))
    for i in range(rows):
        for j in range(columns):
            images_id[i][j] = can.create_image(j*column_width + column_width/2 , i*line_height + line_height/2, image = list[i][j])
       
    attempts_label = tk.Label(playing_window, text="", font=("Helvetica", 20))
    attempts_label.pack(fill = "both", expand=True)     
    countdown_label = tk.Label(playing_window, text="", font=("Helvetica", 20))
    countdown_label.pack(fill = "both", expand=True)
    update_init_countdown(game, can, playing_window, countdown_label, attempts_label,  3, images_id, back_image) #on lance le decompte initiale
    can.bind("<Button-1>", lambda event : on_click(game, event, can, images_id, list, line_height, column_width, back_image, attempts_label, countdown_label, playing_window )) #"<Button-1>" : clic bouton gauche
    display_attempts(game, attempts_label)
    
def display_result(can, playing_window, result): #change la fenetre de jeu pour afficher game over or win 
    bg = '#C597FF'
    can.destroy()
    playing_window.minsize(500,500)
    if (result == 0):
        create_label(playing_window, "GAME OVER", ("Tahoma",20), bg, 'white' )
    if (result == 1):
        create_label(playing_window, "WELL DONE ! YOU WON THIS GAME", ("Tahoma",20), bg, 'white' )
    #playing_window.destroy()
        
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
            display_result(can, playing_window, 0) #0 : le joueur a perdu
        elif (seconds_left >0 and game.is_finished() == (False, True)) : #trop d'essais 
            countdown_label.pack_forget() # on masque le label du chrono
            attempts_label.pack_forget()
            display_result(can, playing_window,0) #0 : le joueur a perdu
        elif (seconds_left >= 0 and game.is_finished() == (True, False)): #fini dans les temps et avec bon nombre d'essais
            countdown_label.pack_forget() # on masque le label du chrono
            attempts_label.pack_forget()
            display_result(can, playing_window, 1) #1 : le joueur a gagne

def display_attempts(game, attempts_label):
    attempts_label.config(text = game.attempts)

def power1(game, can, playing_window, countdown_label, attempts_label): #retire 5s au chrono
    timer = int(countdown_label.cget("text"))
    countdown_label.destroy()
    countdown_label2 = tk.Label(playing_window, text="", font=("Helvetica", 20))
    countdown_label2.pack(fill = "both", expand = True)
    new_timer = timer - 5
    if (new_timer <= 0):
        update_countdown(game, can, playing_window, countdown_label2, attempts_label, 0)
    else :
        update_countdown(game, can, playing_window, countdown_label2, attempts_label, new_timer)

def power2(game, can, playing_window, countdown_label, attempts_label): #ajoute 10s au chrono
    timer = int(countdown_label.cget("text"))
    countdown_label.destroy()
    countdown_label2 = tk.Label(playing_window, text="", font=("Helvetica", 20))
    countdown_label2.pack(fill = "both", expand = True)
    new_timer = timer + 10
    update_countdown(game, can, playing_window, countdown_label2, attempts_label, new_timer)

def power3(game, can, playing_window, images_id, front_images, countdown_label, attempts_label, back_image): 
    new_grid = shuffle_cards(game) #change la grille du jeu 
    #reafficher toutes les cartes : il faut changer images_id et front_images
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
    game.grid = new_grid
    update_init_countdown(game, can , playing_window, countdown_label, attempts_label, 3, new_images_id, back_image)
    return new_images_id, new_front_images

def on_click(game, event, can, images_id, list, line_height, column_width, back_image, attempts_label, countdown_label, playing_window):
    
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
                can.itemconfig(images_id[i][j], image=list[i][j])  # On affiche l'image
                if (card.power == 0):
                    game.flipped.append(card.id)
                    if (len(game.flipped) % 2 == 0):
                        previous_try_id = game.flipped[-2]
                        previous_card = Card.get_card_with_id(previous_try_id)
                        if card.is_pair_of(previous_card) == False:
                            can.after(1000, lambda: hide_unmatched_cards(game, can, images_id, card, previous_card, back_image))
                        else :
                            game.matched_pairs += 1 #une paire en plus est trouvée
                else :
                    if (card.power == 1) :
                        power1(game, can, playing_window, countdown_label, attempts_label)
                    if (card.power == 2) :
                        power2(game, can, playing_window, countdown_label, attempts_label)
                    if (card.power == 3):
                        power3(game, can, playing_window, images_id, list, countdown_label, attempts_label, back_image ) #list est front_images
                    
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