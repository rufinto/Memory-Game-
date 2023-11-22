from cards import *
from classes import *
from interface2 import *
from parameters_choice_interface import *

def main():
    create_all_cards()
    associate_all_pairs(1)
    associate_all_pairs(2)
    associate_all_pairs(3)
    open_pseudo_window()

#while(not game.is_finished()): #tant que le jeu n'est pas terminée on enregistre les choix du joueur 
main()

