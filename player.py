from classes import * 

def init_player_and_game():
    nom = input("Bienvenue dans le jeu Memory\nSaisissez votre pseudo joueur :\n")
    player = Player(nom)
    theme = None
    id_level = 0
    while theme not in [1,2,3] :
        theme = int(input("Choisissez votre thème : (1 : assos de CS, 2 : duos iconiques, 3 : géohgraphie des monuments) : \n"))
    while id_level not in [1,2,3,4] :
        id_level = int(input("Choisissez votre niveau : (1 : 4 paires, 2 : 8 paires, 3 : 10 paires, 4 : 12 paires) : \n"))
    if id_level == 1 :
        level = Level(1, 4, 2, 4)
        game = Game(level, theme)
        return player, game
    elif id_level == 2 :
        level = Level(2, 8, 4, 4)
        game = Game(level, theme)
        return player, game
    elif id_level == 3 :
        level = Level(3, 10, 4, 5)
        game = Game(level, theme)
        return player, game
    elif id_level == 4 :
        level = Level(4, 12, 4, 6)
        game = Game(level, theme)
        return player, game

