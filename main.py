from player import *
from cards import *
from interface2 import display_main_game_interface


def main():
    create_all_cards()
    associate_all_pairs(1)  # on fait que pour le theme 1 et 2
    associate_all_pairs(2)
    associate_all_pairs(3)
    player, game = init_player_and_game()  # initialise le joueur et la partie
    display_main_game_interface(game)


# while(not game.is_finished()): #tant que le jeu n'est pas terminée on enregistre les choix du joueur
main()


# Problèmes avec le jeu :
#     On ne peut pas choisir la difficulté 4
#     Les cartes spéciales apparaiisent toujours au même endroit (ne bas à droite)
#     Les cartes spéciales n'ont aucun effet sur le chronomètre (e.g : après avoir cliqué sur +10 le chrono à l'affichage prend +10 secondes mais le jeu s'arrête quand même lorsqu'il reste 10 secondes affichées)
#     Une fois une des deux cartes +10 utilisée, il est impossible de cliquer sur la deuxième
