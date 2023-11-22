import tkinter as tk
from tkinter import Canvas
from tkinter import ttk
from classes import *
from cards import get_card_position
from cards import get_front_images
from cards import shuffle_cards
from PIL import Image, ImageTk
from cards import *

window_variables = []

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
    print("========ok boutton")

def open_playing_window(game, window, bg, front_images):
    
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
    global message_label
    message_label = tk.Label(playing_window, text="", font=("Helvetica", 16))
    window_variables.append(message_label)
    message_label.pack(fill="both", expand=True)
    
    
    attempts_label = tk.Label(playing_window, text="", font=("Helvetica", 20))
    window_variables.append(attempts_label)
    attempts_label.pack(fill = "both", expand=True)     
    countdown_label = tk.Label(playing_window, text="", font=("Helvetica", 20))
    window_variables.append(countdown_label)
    countdown_label.pack(fill = "both", expand=True)
    
    display_init_fronts(game = game, can = can, playing_window = playing_window, rows = rows, columns = columns, line_height = line_height, column_width = column_width, list = front_images, back_image = back_image, countdown_label = countdown_label, attempts_label = attempts_label, message_widget=message_label)    
    
def display_init_fronts(game, can : Canvas, playing_window, rows, columns, line_height, column_width, list, back_image, countdown_label, attempts_label,message_widget ): #list est la liste des images en format Image
    images_id = []
    for l in list :
        images_id.append(['']*len(l))
    for i in range(rows):
        for j in range(columns):
            images_id[i][j] = can.create_image(j*column_width + column_width/2 , i*line_height + line_height/2, image = list[i][j])
       
    update_init_countdown(game, can, playing_window, countdown_label, attempts_label,  3, images_id, back_image) #on lance le decompte initiale
    can.bind("<Button-1>", lambda event : on_click(game, event, can, images_id, list, line_height, column_width, back_image, attempts_label, countdown_label, playing_window )) #"<Button-1>" : clic bouton gauche
    display_attempts(game, attempts_label)

def display_result(game, can, playing_window, result): #change la fenetre de jeu pour afficher game over or win 
    def restart(game):
        del(game.level)
        del(game)
        open_parameters_window()
    bg = '#C597FF'
    can.destroy()
    playing_window.minsize(500,500)
    frame = create_frame(playing_window, bg, 300, 400, 100, 200)
    if (result == 0):
        create_label(playing_window, "GAME OVER", ("Tahoma",20), bg, 'white' )
    if (result == 1):
        create_label(playing_window, "WELL DONE ! YOU WON THIS GAME", ("Tahoma",20), bg, 'white' )
    add_button(frame, "PLAY AGAIN", font=("Tahoma",20), bg=bg, fg='black', command = lambda : restart(game))
    add_button(frame, "QUIT", font=("Tahoma",20), bg=bg, fg='black', command = lambda : window_variables[0].destroy())    

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

def special1_2(game, can, playing_window, countdown_label, attempts_label, i,message_widget=None):
    
    def special2(playing_window, countdown_label,message_widget): #retire 5s au chrono
        if countdown_label.winfo_exists():  # Vérifie si le label existe encore
            timer = int(countdown_label.cget("text"))
            countdown_label.destroy()
            countdown_label2 = tk.Label(playing_window, text="", font=("Helvetica", 20))
            countdown_label2.pack(fill = "both", expand = True)
            new_timer = timer - 5
            if (new_timer <= 0):
                message_widget.config(text="Oops! Tu as perdu 5 secondes.")
                return (countdown_label2, 0)      
            else :
                return (countdown_label2, new_timer)
        else :
            return None, None

    def special1(playing_window, countdown_label,message_widget): #ajoute 10s au chrono
        if countdown_label.winfo_exists():  # Vérifie si le label existe encore
            timer = int(countdown_label.cget("text"))
            countdown_label.destroy()
            countdown_label2 = tk.Label(playing_window, text="", font=("Helvetica", 20))
            countdown_label2.pack(fill = "both", expand = True)
            new_timer = timer + 10
            message_widget.config(text="Youpi! Tu as gagné 10 secondes.")
            return (countdown_label2, new_timer)
        else :
            return None, None
        
    if (i == 1) :
        countdown_label, new_timer = special1(playing_window, countdown_label,message_widget)
    elif (i == 2) :
        countdown_label, new_timer = special2(playing_window, countdown_label,message_widget)
    if (countdown_label, new_timer) != (None, None) :
        update_countdown(game, can, playing_window, countdown_label, attempts_label, new_timer)
    return countdown_label

def special4(game, can, playing_window, images_id, front_images, countdown_label, attempts_label, back_image,message_label): 
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
    message_label.config(text="La grille est mélangée")
    return new_images_id, new_front_images

def special3(game, can, images_id, list,message_label):#elle affiche une pair
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
            message_label.config(text="Une paire est affichée!!")
            return i,j

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
                    if card.power == 1:
                        window_variables[3] = special1_2(game, can, playing_window, countdown_label, attempts_label,1,message_label)
                    elif card.power == 2:
                        window_variables[3] = special1_2(game, can, playing_window, countdown_label, attempts_label, 2,message_label)
                    if (card.power == 3):
                        game.flipped.append(card.id) 
                        special3(game, can, images_id, list)
                        
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

def open_pseudo_window():
    def init_player():
        player = Player(pseudo.get())
        print(player.name)
        name.destroy()
        open_parameters_window()
    name = tk.Tk()
    name.minsize(600,600)
    name.title('Choose a pseudo')
    background_image = Image.open("fond1.jpg")  # Remplacez "votre_image.jpg" par le chemin de votre image
    background_image = ImageTk.PhotoImage(background_image)

    background_label = tk.Label(name, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    pseudo = tk.StringVar()
    pseudo = tk.StringVar()
    tk.Label(name,text = 'Pseudo',font=("Tahoma",20)).place(relx = 0.2, rely = 0.4, anchor = tk.CENTER)
    pseudo = tk.Entry(name)
    pseudo.place(relx=0.45, rely = 0.4, anchor = tk.CENTER)
    tk.Button(name, text = 'Quit', command = name.quit,font=("Tahoma",20)).place(relx=0.5, rely=0.85, anchor=tk.CENTER)
    tk.Button(name, text = 'Confirm', command=init_player,font=("Tahoma",20)).place(relx = 0.8, rely = 0.4, anchor = tk.CENTER)
    name.mainloop()

def open_parameters_window(): 
    level_window = create_window('Choose difficulty', '#C597FF')
    id_level_var = tk.IntVar()
    def ShowChoice():
        level_window.destroy()
        if id_level_var.get() == 1:
            level_var = Level(id = 1, nb_pairs = 4, nb_row = 2, nb_column = 4)
        elif id_level_var.get() == 2:
            level_var = Level(id = 2, nb_pairs = 7, nb_row = 4, nb_column = 4)
        elif id_level_var.get() == 3:
            level_var = Level(id = 3, nb_pairs = 9, nb_row = 4, nb_column = 5)
        elif id_level_var.get() == 4:
            level_var = Level(id = 4, nb_pairs = 10, nb_row = 4, nb_column = 6)
        def init_globale():
            theme = theme_var.get()
            print(theme)
            game = Game(level_var,theme)
            theme_window.destroy()
            display_main_game_interface(game)
        theme_window = create_window('Select a theme','#C597FF')
        theme_var = tk.IntVar()
        tk.Label(theme_window, text = 'Select theme',font=("Tahoma",20)).place(relx = 0.5, rely = 0.2, anchor = tk.CENTER)
        tk.Radiobutton(theme_window,text = "assos CS",value=1,variable=theme_var,command=init_globale,font=("Tahoma",20)).place(relx = 0.5, rely = 0.4, anchor = tk.CENTER)
        tk.Radiobutton(theme_window,text = "duos iconiques",value=2,variable=theme_var,command=init_globale,font=("Tahoma",20)).place(relx = 0.5, rely = 0.6, anchor = tk.CENTER)
        tk.Radiobutton(theme_window,text = "géographie des monuments",value=3,variable=theme_var,command=init_globale,font=("Tahoma",20)).place(relx = 0.5, rely = 0.8, anchor = tk.CENTER)
    tk.Label(level_window, text = 'Select difficulty',font=("Tahoma",20)).place(relx = 0.5, rely = 0.2, anchor = tk.CENTER)
    tk.Radiobutton(level_window,text = "4 paires",value=1,variable=id_level_var,command=ShowChoice,font=("Tahoma",20)).place(relx = 0.25, rely = 0.45, anchor = tk.CENTER)
    tk.Radiobutton(level_window,text = "8 paires",value=2,variable=id_level_var,command=ShowChoice,font=("Tahoma",20)).place(relx = 0.25, rely = 0.7, anchor = tk.CENTER)
    tk.Radiobutton(level_window,text = "10 paires",value=3,variable=id_level_var,command=ShowChoice,font=("Tahoma",20)).place(relx = 0.75, rely = 0.45, anchor = tk.CENTER)
    tk.Radiobutton(level_window,text = "12 paires",value=4,variable=id_level_var,command=ShowChoice,font=("Tahoma",20)).place(relx = 0.75, rely = 0.7, anchor = tk.CENTER)
    tk.mainloop()

def display_main_game_interface(game):
    if (len(window_variables) > 0):
        window_variables[0].destroy()
    bg = '#C597FF'
    path = "3997691.png"
    window = create_window("Memory Game", bg)
    window_variables.append(window)
    create_label (window,"MEMORY GAME", ("Tahoma",40), bg, 'white')
    image = Image.open(path)
    image = ImageTk.PhotoImage(image)
    create_icanva(window, bg, 250, 250, 250, 250, image)
    frame = create_frame(window, bg, 400, 250, 5, 30)
    front_images = get_front_images(game)
    add_button(frame, "PLAY", font=("Tahoma",20), bg=bg, fg='black', command = lambda : open_playing_window(game, window, bg, front_images))
    window.mainloop()
    
    