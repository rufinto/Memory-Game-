from classes import * 

def init_player_and_game():
    nom = input("Bienvenue dans le jeu Memory\nSaisissez votre pseudo joueur :\n")
    player = Player(nom)
    theme = None
    id_level = 0
    while theme not in [1,2,3] :
        theme = int(input("Choisissez votre thème : (1 : assos de CS, 2 : duos iconiques, 3 : géographie des monuments) : \n"))
    while id_level not in [1,2,3,4] :
        id_level = int(input("Choisissez votre niveau : (1 : 4 paires, 2 : 8 paires, 3 : 10 paires, 4 : 12 paires) : \n"))
    if id_level == 1 :
        level = Level(id = 1, nb_pairs = 4, nb_row = 2, nb_column = 4)
        game = Game(level, theme)
        return player, game
    elif id_level == 2 :
        level = Level(id = 2, nb_pairs = 8, nb_row = 4, nb_column = 4)
        game = Game(level, theme)
        return player, game
    elif id_level == 3 :
        level = Level(id = 3, nb_pairs = 10, nb_row = 4, nb_column = 5)
        game = Game(level, theme)
        return player, game
    elif id_level == 4 :
        level = Level(id = 4, nb_pairs = 12, nb_row = 4, nb_column = 6)
        game = Game(level, theme)
        return player, game

