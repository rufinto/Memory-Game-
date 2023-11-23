from cards_mvp import create_all_cards
from cards_mvp import associate_all_pairs

from classes_mvp import *
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
    associate_all_pairs(1)
    associate_all_pairs(2)
    associate_all_pairs(3)
    game = init_game_mvp()
    display_main_game_interface_mvp(game)
    
main()
