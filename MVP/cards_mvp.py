from classes_mvp import *
import tkinter as tk
from PIL import Image, ImageTk
import random as rd

def create_all_cards(): 
    Card(0, None, None, None) #creation of a card where card.id = 0 in order that the id of each card has the same value as its index in the list of the cards
    
    #creation of cards for theme 1
    back_image_path = "DATA_MVP/IMAGES/back1.png"
    for i in range(1, 21):
        front_image_path = "DATA_MVP/IMAGES/" + str(i) + ".png"
        Card(id = i, front = front_image_path, back = back_image_path, theme = 1)
    for i in range(41, 61): #same image but duplicated
        front_image_path = "DATA_MVP/IMAGES/" + str(i) + ".png"
        Card(id = i, front = front_image_path, back = back_image_path, theme = 1)
    
    #creation of cards for theme 2
    back_image_path = "DATA_MVP/IMAGES/back2.png"
    for i in range(21, 41):
        front_image_path = "DATA_MVP/IMAGES/" + str(i) + ".png"
        Card(id = i, front = front_image_path, back = back_image_path, theme = 2)
    for i in range(61, 83):
        front_image_path = "DATA_MVP/IMAGES/" + str(i) + ".png"
        Card(id = i, front = front_image_path, back = back_image_path, theme = 2)
    for i in range(152, 174):
        front_image_path = "DATA_MVP/IMAGES/" + str(i) + ".png"
        Card(id = i, front = front_image_path, back = back_image_path, theme = 2)
    
    #creation of cards for theme 3
    back_image_path = "DATA_MVP/IMAGES/back3.png"
    for i in range(84, 150):
        front_image_path = "DATA_MVP/IMAGES/" + str(i) + ".png"
        Card(id = i, front = front_image_path, back = back_image_path, theme =3)
    

def associate_all_pairs(theme) -> None :
    CARDS = Card.get_cards() #we fetch the list of all the cards
    THEMES = Card.get_themes() #we fetch the dictionary that contains the themes 
    pairs = THEMES[theme] #we only keep the list of tuples associated with the theme
    for (i,j) in pairs: #for each pair
        card1 = Card.get_card_with_id(i) #we fetch the id of the first card
        card2 = Card.get_card_with_id(j) #we fetch the id of its pair
        card1.pair = card2.id #the attribute None becomes the id of the pair 
        card2.pair = card1.id 


def get_front_images(game): #return a list of the front images of the cards of the grid
    front_images = []
    grid = game.grid #we fetch the grid of the game
    for l in grid :
        front_images.append(['']*len(l)) 
    nb_rows = game.level.nb_row #we fetch the number of rows of the game
    nb_columns = game.level.nb_column #we fetch the number of columns of the game
    for i in range(nb_rows):
        for j in range(nb_columns):
            card = Card.get_card_with_id(grid[i][j]) #we fetch the card in position (i,j)
            front_image = Image.open(card.front) #opening of the front image associated to the card
            front_image = ImageTk.PhotoImage(front_image) #displaying 
            front_images[i][j] = front_image #indices in the list front_images are the same as indices in grid
    return front_images


def get_card_position(game, id : int) -> tuple : #return the row and the column in which the card is positioned 
    for i in range(game.level.nb_row):
        for j in range(game.level.nb_column):
            if (game.grid[i][j] == id) :
                return i,j 


def shuffle_cards(game): #return a grid built from the same game but with cards placed in other positions 
    grid = []
    cards = game.cards.copy() #we copy the list of the game cards 
    for l in game.grid :
        grid.append([0]*len(l)) #initialisation of the grid 
    for i in range(game.level.nb_row):
        for j in range(game.level.nb_column):
            id = rd.choice(cards) #we randomly choose an id within the ids of the game cards 
            grid[i][j] = id #the id is re-attributed to a position... 
            cards.remove(id) #...and removed from the list in which the choice is made
    return grid
