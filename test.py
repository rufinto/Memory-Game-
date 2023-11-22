class Level :
    def __init__(self, id, nb_pairs, nb_row, nb_column):
        self.id = id
        self.nb_pairs = nb_pairs
        self.nb_row = nb_row
        self.nb_column = nb_column
        self.timer = id*20 #time the player has before losing the game 
        self.max_attempts = 4*nb_pairs
    
    def Id(self):
        return self.id
    
    def Nb_row(self):
        return self.nb_row
    
    def Nb_column(self):
        return self.nb_column
    
    
    
level1 = Level(1, 2, 3, 4)

#del(level1)
print(level1.nb_pairs)