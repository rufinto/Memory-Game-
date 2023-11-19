from player import *
from cards import *
from interface2 import display_main_game_interface

def main():
    create_all_cards()
    associate_all_pairs(1) #on fait que pour le theme 1 
    player, game = init_player_and_game() #initialise le joueur et la partie
    display_main_game_interface(game)
    
#while(not game.is_finished()): #tant que le jeu n'est pas terminée on enregistre les choix du joueur 
main()