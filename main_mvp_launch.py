from player import *
from cards import *
from interface_mvp import *

def init_game_mvp():
    theme = 0
    while(theme not in [1,2,3]):
        theme = int(input("Choose your theme : 1 (CS associations), 2 (Cinema), 3 (Geography)\n"))
    level = Level(1, 4, 2, 4)
    game = Game(level, theme)
    return game

def main():
    create_all_cards()
    associate_all_pairs(1)  # on fait que pour le theme 1 et 2
    associate_all_pairs(2)
    associate_all_pairs(3)
    game = init_game_mvp()  # initialise le joueur et la partie
    display_main_game_interface_mvp(game)
    
main()
