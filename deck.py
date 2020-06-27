#v4

import random
from card import Card

class Deck:
    def __init__(self):
        self.contents = []
        
    def add(self, card):
        self.contents.append(card)
        
    def get(self, index):
        return self.contents[index]
    
    def remove(self, index):
        self.contents.pop(index)
        
    def getremove(self, index):
        return self.contents.pop(index)
        
class Main_Deck:
    def __init__(self):
        super().__init__()
        for i in ['heart', 'spade', 'diamd', 'clove']:
            for j in range(1, 14):
                self.contents.append(Card(i, j).flip())
        random.shuffle(self.contents)