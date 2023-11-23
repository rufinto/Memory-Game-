from cards import *
from classes import *
from play import *

def main():
    create_all_cards()
    associate_all_pairs(1) #on fait que pour le theme 1 et 2
    associate_all_pairs(2)
    associate_all_pairs(3)
    display_main_game_interface()

#while(not game.is_finished()): #tant que le jeu n'est pas terminée on enregistre les choix du joueur 
main()
