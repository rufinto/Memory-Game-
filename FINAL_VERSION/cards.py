from classes import Card
from classes import Game
import tkinter as tk
from PIL import Image, ImageTk
import random as rd

#creates all the cards that appear in the game
#returns nothing
def create_all_cards() -> None:
    Card(0, None, None, None) #create a card identified by 0, to have each position equals id in CARDS
    
    #creation of cards for theme 1 :
    back_image_path = "DATA/IMAGES/back1.png" 
    for i in range(1, 21):
        front_image_path = "DATA/IMAGES/" + str(i) + ".png"
        Card(id = i, front = front_image_path, back = back_image_path, theme = 1)
    for i in range(41, 61):
        front_image_path = "DATA/IMAGES/" + str(i) + ".png"
        Card(id = i, front = front_image_path, back = back_image_path, theme = 1)
    
    #creation of cards for theme 2 :
    back_image_path = "DATA/IMAGES/back2.png"
    for i in range(21, 41):
        front_image_path = "DATA/IMAGES/" + str(i) + ".png"
        Card(id = i, front = front_image_path, back = back_image_path, theme = 2)
    for i in range(61, 83):
        front_image_path = "DATA/IMAGES/" + str(i) + ".png"
        Card(id = i, front = front_image_path, back = back_image_path, theme = 2)
    for i in range(152, 174):
        front_image_path = "DATA/IMAGES/" + str(i) + ".png"
        Card(id = i, front = front_image_path, back = back_image_path, theme = 2)
    
    #creation of cards for theme 3 : 
    back_image_path = "DATA/IMAGES/back3.png"
    for i in range(84, 150):
        front_image_path = "DATA/IMAGES/" + str(i) + ".png"
        Card(id = i, front = front_image_path, back = back_image_path, theme =3)
    
    #creation of special cards :
    Card(id = 200, front = "DATA/IMAGES/power1.png", back = '', theme = 0, power = 1) # +10
    Card(id = 201, front = "DATA/IMAGES/power2.png", back = '', theme = 0, power = 2) # -5
    Card(id = 202, front = "DATA/IMAGES/power3.png", back = '', theme = 0, power = 3) # reveal a pair
    Card(id = 203, front = "DATA/IMAGES/power4.png", back = '', theme = 0, power = 4) #shuffle

#for each card of theme, we associate its pair :
def associate_all_pairs(theme) -> None :
    CARDS = Card.get_cards() #we fetch the list of all the cards
    THEMES = Card.get_themes() #we fetch the dictionary that contains the themes 
    pairs = THEMES[theme] #we only keep the list of tuples associated with the theme
    for (i,j) in pairs: #for each pair
        card1 = Card.get_card_with_id(i) #we fetch the id of the first card
        card2 = Card.get_card_with_id(j) #we fetch the id of its pair
        card1.pair = card2.id #the attribute None becomes the id of the pair 
        card2.pair = card1.id 

#returns a list of all the front images in the grid as imageTk.PhotoImage :
def get_front_images(game : Game) -> list:
    front_images = []
    grid = game.grid
    for l in grid :
        front_images.append(['']*len(l))
    nb_rows = game.level.nb_row 
    nb_columns = game.level.nb_column
    for i in range(nb_rows):
        for j in range(nb_columns):
            card = Card.get_card_with_id(grid[i][j])
            front_image = Image.open(card.front)
            front_image = ImageTk.PhotoImage(front_image)
            front_images[i][j] = front_image
    return front_images

#returns the row and the column in which the card is positioned in the grid :
def get_card_position(game : Game, id : int) -> tuple : 
    for i in range(game.level.nb_row):
        for j in range(game.level.nb_column):
            if (game.grid[i][j] == id) :
                return i,j 

#returns a shuffled version of the grid
def shuffle_cards(game : Game) -> list: 
    grid = []
    cards = game.cards.copy()
    for l in game.grid :
        grid.append([0]*len(l))
    for i in range(game.level.nb_row):
        for j in range(game.level.nb_column):
            id = rd.choice(cards)
            grid[i][j] = id
            cards.remove(id)
    return grid
