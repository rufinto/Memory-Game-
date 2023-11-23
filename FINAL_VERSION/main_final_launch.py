from cards import *
from classes import *
from play import *

def main():
    create_all_cards() #creation of all cards
    associate_all_pairs(1) #association of pairs from theme 1 (assos)
    associate_all_pairs(2) #association of pairs from theme 2 (cinéma)
    associate_all_pairs(3) #association of pairs from theme 3 (géographie)
    display_main_game_interface() #launch

main()