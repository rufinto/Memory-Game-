import random as rd

class Card :
    CARDS = []

    THEMES = {
    1: [
        (1, 41), (2, 46), (3, 42), (4, 47), (5, 49), (6, 54), (7, 56), (8, 58), (9, 48), 
        (10, 45), (11, 55), (12, 50), (13, 51), (14, 52), (15, 43), (16, 53), 
        (17, 57), (18, 59), (19, 60), (20, 44)
    ],
    2: [
        (21, 77), (22, 39), (23, 72), (24, 38), (25, 61), (26, 64), (27, 32), 
        (28, 34), (29, 33), (30, 31), (35, 36), (37, 71), (40, 62), (63, 70), 
        (65, 69), (66, 67), (68, 82), (73, 78), (74, 76), (75, 80), (79, 81), (152, 153), (154, 155), (156, 157), (158, 159), (160, 169), (161, 163), (162, 164), (165, 166), (167, 168), (170, 171), (172, 173) 
    ], 
    3: [
        (84, 85), (86, 87), (88, 89), (90, 91), (92, 93), (94, 95), (96, 97), (98, 99), (100, 101), 
        (102, 103), (104, 105), (106, 107), (108, 109), (110, 111), (112, 113), (114, 115), 
        (116, 117), (118, 119), (120, 121), (122, 123), (124, 125), (126, 127), (128, 129), (130, 131),
        (132, 133), (134, 135), (136, 137), (138, 139), (140, 141), (142, 143), (144, 145), (146, 147), 
        (148, 149)
    ]
}
    def __init__(self, id, front, back, theme, flipped = False, pair = None, power = 0):
        self.id = id
        self.front = front
        self.back = back
        self.theme = theme
        self.flipped = flipped # False if the card is hidden
        self.pair = pair #id of its pair
        self.power = power #0 if it is not a special card
        Card.CARDS.append(self)
    
    def is_pair_of(self, card):
        return self.pair is card.id
    
    def is_flipped(self): #return True if the card is flipped 
        return self.flipped is True
    
    def flip(self):
        self.flipped = not self.flipped
        
    @classmethod
    def get_card_with_id(cls,id):
        for card in cls.CARDS :
            if card.id == id:
                return card
    
    @classmethod
    def get_cards(cls):
        return cls.CARDS
    
    @classmethod
    def get_themes(cls):
        return cls.THEMES
    
    
class Level :
    def __init__(self, id, nb_pairs, nb_row, nb_column):
        self.id = id
        self.nb_pairs = nb_pairs
        self.nb_row = nb_row
        self.nb_column = nb_column
    
class Game :
    def __init__(self, level : Level, theme):
        self.level = level
        self.theme = theme
        self.cards = [] #list of the cards id in the game 
        self.attempts = 0
        self.flipped = [] #list of the cards id which are flipped
        self.matched_pairs = 0 #number of pairs discovered 
        self.grid = [] #list of list containing the cards id that are in the grid
        self.started = False
        self.init_game()
        self.init_grid()
        
    def init_game(self):
        level = self.level
        nb_pairs = level.nb_pairs
        pairs = rd.sample(Card.THEMES[self.theme], k = nb_pairs)
        for (i,j) in pairs :
            self.cards.append(i)
            self.cards.append(j)
        rd.shuffle(self.cards)
            
    def init_grid(self):
        grid = []
        level = self.level
        nb_row = level.nb_row
        nb_column = level.nb_column
        cards = self.cards.copy()
        rd.shuffle(cards)
        for i in range(0,(nb_row-1)*nb_column + 1, nb_column ):
            grid.append(cards[i:i+nb_column])
        self.grid = grid

    def is_finished(self): #game over if all pairs have been discovered or all attemps have been used 
        return (self.matched_pairs is self.level.nb_pairs)

    def get_back(self):
        return "DATA_MVP/IMAGES/back" + str(self.level.id) + ".png"