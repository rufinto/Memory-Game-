from cards_mvp import create_all_cards
from cards_mvp import associate_all_pairs

from classes_mvp import *
from interface_mvp import *

def init_game_mvp(): #initialisation of the game
    theme = 0
    while(theme not in [1,2,3]):
        theme = int(input("Choose your theme : 1 (CS associations), 2 (Cinema), 3 (Geography)\n")) #input of the theme in the terminal
    level = Level(1, 4, 2, 4) #default : the easiest one 
    game = Game(level, theme) #creation of the game 
    return game

def main():
    create_all_cards() #creation of all cards
    associate_all_pairs(1) #association of pairs from theme 1 (assos)
    associate_all_pairs(2) #association of pairs from theme 2 (cinéma)
    associate_all_pairs(3) #association of pairs from theme 3 (géographie)
    game = init_game_mvp() #initialisation of the game 
    display_main_game_interface_mvp(game) #launch
    
main()
