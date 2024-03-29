from classes import * 

def init_game(id_level, theme): #return the game considering the level difficulty and theme choosen 
    if id_level == 1 : #the easiest level
        level = Level(id = 1, nb_pairs = 4, nb_row = 2, nb_column = 4)
        game = Game(level, theme)
        return game
    elif id_level == 2 : #level 2
        level = Level(id = 2, nb_pairs = 7, nb_row = 4, nb_column = 4)
        game = Game(level, theme)
        return game
    elif id_level == 3 : #level 3
        level = Level(id = 3, nb_pairs = 9, nb_row = 4, nb_column = 5)
        game = Game(level, theme)
        return game
    elif id_level == 4 :#the hardest level 
        level = Level(id = 4, nb_pairs = 11, nb_row = 4, nb_column = 6)
        game = Game(level, theme)
        return game