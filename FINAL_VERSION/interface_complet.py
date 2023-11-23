import tkinter as tk
from tkinter import Canvas
from tkinter import ttk
from PIL import Image, ImageTk

from classes import *

from cards import get_card_position
from cards import shuffle_cards

import time 

from sounds import *

window_variables = []
#format : [window]
image_variables = []
#format : [front_images, images_id]
SHUFFLE = False


#Tkinter functions used to simplify later functions (creation of window, label, frame, grid, button, icanva)

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
    
def create_grid(window, width, height, bg, rows, columns): #create a canva with a grid 
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

def create_icanva(window, bg, w, h, x, y, image):
    can= tk.Canvas(window, width=w, height= h ,bg = bg,bd=0)
    can.place(x=x, y=y)
    can.create_image (w//2, h//2, image=image) #w//2 and h//2 are the image position on the canva
    can.pack(expand='Yes')


#launch of the game interface 

def open_playing_window(game, window, i_variables, bg, front_images, start, frame):
    play_sound(sound_button)
    start.destroy()
    frame.destroy()
    global image_variables
    image_variables = i_variables
    
    rows = game.level.nb_row
    columns = game.level.nb_column
    line_height = 700//rows  #height of each line
    column_width = 700//columns #width of each column 
    
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
    
def display_init_fronts(game, can : Canvas, playing_window, rows, columns, line_height, column_width, list, back_image, countdown_label, attempts_label  ): #list : list of images 
    images_id = []
    for l in list :
        images_id.append(['']*len(l))
    for i in range(rows):
        for j in range(columns):
            images_id[i][j] = can.create_image(j*column_width + column_width/2 , i*line_height + line_height/2, image = list[i][j])
    
    image_variables.append(images_id)

    update_init_countdown(game, can, playing_window, countdown_label, attempts_label,  3, images_id, back_image) #we launch an initial countdown of 3 secondes 
    can.bind("<Button-1>", lambda event : on_click(game, event, can, line_height, column_width, back_image, attempts_label, countdown_label, playing_window )) #"<Button-1>" : click left button 
    display_attempts(game, attempts_label)
    
def display_result(game, can, playing_window, result): #replace the playing window by a window that indicates the player whether he has won or lost 
    bg = '#C597FF'
    can.destroy()
    playing_window.minsize(500,500)
    frame = create_frame(playing_window, bg, 300, 400, 100, 200)
    if (result == 0): #game lost 
        create_label(playing_window, "GAME OVER", ("Tahoma",20), bg, 'white' )
    if (result == 1): #game won 
        create_label(playing_window, "WELL DONE ! YOU WON THIS GAME", ("Tahoma",20), bg, 'white' )
    add_button(frame, "PLAY AGAIN", font=("Tahoma",20), bg=bg, fg='black', command = lambda : play_again(game, playing_window, can)) #allows the player to play again with differents parameters
    add_button(frame, "QUIT", font=("Tahoma",20), bg=bg, fg='black', command = lambda : window_variables[0].destroy()) #to quit the game 
    
def play_again(game, playing_window, can): #allows the player to restrart a new game with differents parameters (level and theme) choices 
    can.destroy()
    playing_window.destroy()
    global SHUFFLE #call to the global variable 
    SHUFFLE = False
    for id in game.cards : #classic cards
        card = Card.get_card_with_id(id)
        card.flipped = False
    for id in game.special_cards : #special cards
        card = Card.get_card_with_id(id)
        card.flipped = False
    
def update_init_countdown(game, can, playing_window, countdown_label, attempts_label, seconds_left, images_id, back_image): #to update the initial countdown
    countdown_label.config(text=str(seconds_left))
    if seconds_left > 0: #if there is time left
        playing_window.after(1000, lambda: update_init_countdown(game, can, playing_window, countdown_label, attempts_label, seconds_left - 1, images_id, back_image)) #new call to the function after 1 second
    else: #after the 3 secondes, the game can start
        for list in images_id: 
            for image_id in list : 
                can.itemconfig(image_id, image = back_image)
        game.started = True
        update_countdown(game, can, playing_window, countdown_label, attempts_label, game.level.timer) #launch of the countdown depending on the level difficulty
     
def update_countdown(game, can, playing_window, countdown_label, attempts_label, seconds_left): #to update the countdown
    if countdown_label.winfo_exists():  #Check whether the label still exists 
        countdown_label.config(text=str(seconds_left))
        if (seconds_left > 0 and game.is_finished() == (False, False)) :
            playing_window.after(1000, lambda: update_countdown(game, can, playing_window, countdown_label, attempts_label, seconds_left - 1))
        elif (seconds_left <= 0 and game.is_finished() == (False, False)): #no time left and not all pairs have been recomposed 
            countdown_label.pack_forget() #we hide the countdown label 
            attempts_label.pack_forget()
            display_result(game, can, playing_window, 0) #0 : the player has lost
        elif (seconds_left >0 and game.is_finished() == (False, True)) : #too much attempts
            countdown_label.pack_forget() #we hide the countdown label
            attempts_label.pack_forget()
            display_result(game, can, playing_window,0) #0 : the player has lost
        elif (seconds_left >= 0 and game.is_finished() == (True, False)): #countdown not finished and the numbers of attempts have not been overcomed
            countdown_label.pack_forget() #we hide the countdown label
            attempts_label.pack_forget()
            display_result(game, can, playing_window, 1) #1 : the player has won

def display_attempts(game, attempts_label): 
    attempts_label.config(text = game.level.max_attempts - game.attempts)

def special1_2(game, can, playing_window, countdown_label, attempts_label, i): #special cards associated with the managing of the countdown
    
    def special2(playing_window, countdown_label): #delete 5 seconds from the countdown 
        if countdown_label.winfo_exists():  #Check whether the label still exists
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

    def special1(playing_window, countdown_label): #add 10 seconds to the countdown
        if countdown_label.winfo_exists():  #Check whether the label still exists
            play_sound(sound_good)
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
    message_text = "The cards are being shuffeled...."
    play_sound(sound_shuffle)
    message_frame = tk.Frame(can, bd=5, relief=tk.SOLID)
    message_frame.place(relx=0.5, rely=0.5, anchor="center")
    message_element = tk.Label(message_frame, text=message_text, font=("Helvetica", 20), fg="black")
    message_element.pack(padx=10, pady=10) 
    playing_window.update()
    time.sleep(1)
    message_frame.destroy()
    
    new_grid = shuffle_cards(game) #change the game grid
    rows = game.level.nb_row
    columns = game.level.nb_column
    line_height = 700//rows  #height of each line
    column_width = 700//columns #width of each column
    new_images_id = []
    new_front_images = []
    
    for l in new_grid :
        new_images_id.append([0]*len(l))
        new_front_images.append([0]*len(l))
        
    for i in range(rows):
        for j in range(columns):
            new_id = new_grid[i][j] #id of the card to position at coordinates i,j
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

def special3(game, playing_window, can, images_id, list):#reveal a pair
    play_sound(sound_good)
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
        x,y = event.x, event.y #coordonnes of the click
        row = int(y)// line_height #line of the click
        column = int(x)// column_width #column of the click
        #check whether the player has clicked on the image or on a blanck space :
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
            if not card.flipped and card.id not in game.flipped:  #Check whether the card is not already flipped or associated to its pair
                card.flipped = True
                can.itemconfig(images_id[i][j], image = list[i][j])  #we display the image
                play_sound(sound_flip)
                if (card.power == 0): #not a special card
                    game.flipped.append(card.id) #we don't add the special cards to the flipped ones (not a pair) except from the number 3 (the one used to reveal a pair)
                    if ((len(game.flipped) % 2 == 0 and 202 not in game.flipped)):
                        previous_try_id = game.flipped[-2]
                        previous_card = Card.get_card_with_id(previous_try_id)
                        if card.is_pair_of(previous_card) == False:
                            play_sound(sound_wrongpair)                  
                            can.after(1000, lambda: hide_unmatched_cards(game, can, images_id, card, previous_card, back_image))
                        else :
                            game.matched_pairs += 1 #a pair has been discovered
                            play_sound(sound_rightpair)                  
                    elif (202 in game.flipped and len(game.flipped) % 2 == 0) : #we already had a pair
                        game.flipped.remove(202) #we remove the special card 3
                    elif (202 in game.flipped and (len(game.flipped) -1 ) % 2 == 0) : #we did not have a pair
                        game.flipped.remove(202) #we remove the special card 3
                        previous_try_id = game.flipped[-4] #we don't consider the pair added
                        previous_card = Card.get_card_with_id(previous_try_id)
                        if card.is_pair_of(previous_card) == False:
                            can.after(1000, lambda: hide_unmatched_cards(game, can, images_id, card, previous_card, back_image))
                        else :
                            game.matched_pairs += 1 #a pair has been discovered
                else : #a special card
                    global SHUFFLE
                    if (card.power == 1): #5 seconds less
                        special1_2(game, can, playing_window, countdown_label, attempts_label, 1)
                    elif (card.power == 2): #10 seconds more
                        special1_2(game, can, playing_window, countdown_label, attempts_label, 2)
                    elif (card.power == 3): #pair reveal
                        game.flipped.append(card.id) 
                        special3(game, playing_window, can, images_id, list)
                    elif (card.power == 4 and SHUFFLE == False ): #shuffle
                        SHUFFLE = True
                        special4(game, playing_window, can, list, back_image)
                        
def hide_unmatched_cards(game, can, images_id, card, previous_card, back_image): #to flip back cards that don't match 
    i, j = get_card_position(game, card.id)
    can.itemconfig(images_id[i][j], image=back_image)  #Flip the current card

    k, l = get_card_position(game, previous_card.id)
    can.itemconfig(images_id[k][l], image=back_image)  #Flip the previous one (not its pair)

    #Re-initialisation of the cards that have not been discovered 
    card.flipped = False
    previous_card.flipped = False
    game.flipped.remove(card.id)
    game.flipped.remove(previous_card.id)
