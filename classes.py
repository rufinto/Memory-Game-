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
        (65, 69), (66, 67), (68, 82), (73, 78), (74, 76), (75, 80), (79, 81)
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
        self.flipped = flipped # = False si la carte est cachée
        self.pair = pair #identifiant de sa paire
        self.power = power #0 si ce n'est pas une carte spéciale
        Card.CARDS.append(self)
    
    #si power = 1 : on retire 5s au chrono
    #si power = 2 : on ajoute 5s au chrono
    #si power = 3 : on remélange toutes les cartes
    #si power = 4 : on retourne toutes les cartes pendant 3s et le chrono s'arrete pendant ce temps
    #si power = 5 : on retourne une paire
    
    def is_pair_of(self, card):
        return self.pair is card.id
    
    def is_flipped(self): #renvoie vraie si la carte est visible
        return self.flipped is True
    
    def flip(self): #
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
        self.timer = id*20 #temps max qu'on donne pour résoudre les paires
        self.max_attempts = 4*nb_pairs
        
    def get_back_file(self):
        return "back"+self.id+".png"
    
class Game :
    def __init__(self, level : Level, theme):
        self.level = level
        self.theme = theme
        self.cards = [] #liste des identifiants des cartes dans la game
        self.attempts = 0
        self.flipped = [] #liste des identifiants des cartes qui sont visibles
        self.matched_pairs = 0 #nombre de paires trouvés
        self.grid = [] #liste de listes avec les identifiants des cartes qui sont dans la grille
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
        for i in range(0,(nb_row-1)*nb_column + 1, nb_column ):
            grid.append(self.cards[i:i+nb_column])
        self.grid = grid
    
    def is_finished(self): #jeu fini si toutes les paires sont trouvees ou bien nombre max d'essais atteint
        return (self.matched_pairs is self.level.nb_pairs, self.attempts >= self.level.max_attempts)

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    