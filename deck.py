import random
from card import Card

class Deck:
    def __init__(self):
        self.contents = []
        
class Main_Deck:
    def __init__(self):
        super().__init__()
        for i in ['heart', 'spade', 'diamd', 'clove']:
            for j in range(1, 14):
                self.contents.append(Card(i, j))
                self.contents[-1].hidden = True
        random.shuffle(self.contents)