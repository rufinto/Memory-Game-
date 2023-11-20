from classes import Card
import tkinter as tk
from PIL import Image, ImageTk
import random as rd

def create_all_cards():
    card = Card(0, None, None, None) #cree une carte identifié 0 juste pour pas avoir de degalage des nombres
    back_image_path = "IMAGES/back1.png"
    for i in range(1, 21):
        front_image_path = "IMAGES/" + str(i) + ".png"
        card = Card(id = i, front = front_image_path, back = back_image_path, theme =1)
    for i in range(41, 61):
        front_image_path = "IMAGES/" + str(i) + ".png"
        card = Card(id = i, front = front_image_path, back = back_image_path, theme =1)
    
    back_image_path = "IMAGES/back2.png"
    for i in range(21, 41):
        front_image_path = "IMAGES/" + str(i) + ".png"
        card = Card(id = i, front = front_image_path, back = back_image_path, theme =2)
    for i in range(61, 83):
        front_image_path = "IMAGES/" + str(i) + ".png"
        card = Card(id = i, front = front_image_path, back = back_image_path, theme =2)

    back_image_path = "IMAGES/back3.png"
    for i in range(84, 150):
        front_image_path = "IMAGES/" + str(i) + ".png"
        card = Card(id = i, front = front_image_path, back = back_image_path, theme =3)
    
    #test carte speciale 2 :
    card = Card(id = 100, front = "IMAGES/special1.png", back = back_image_path, theme =2, power = 3)
    
def associate_all_pairs(theme) -> None :
    CARDS = Card.get_cards() #we fetch the list of all the cards
    THEMES = Card.get_themes() #we fetch the dictionary that cointains the themes 
    pairs = THEMES[theme] #we only keep the list of tuples associated with the theme
    for (i,j) in pairs: #for each pair
        card1 = Card.get_card_with_id(i) #we fetch the id of the first card
        card2 = Card.get_card_with_id(j) #we fetch the id of its pair
        card1.pair = card2.id #the attribute None becomes the id of the pair 
        card2.pair = card1.id 

def get_front_images(game): #renvoie une liste de toutes les images face des cartes de la grille, meme indices que la grille
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

def get_card_position(game, id):
    for i in range(game.level.nb_row):
        for j in range(game.level.nb_column):
            if (game.grid[i][j] == id) :
                return i,j

def shuffle_cards(game): #melange toutes les cartes
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
                