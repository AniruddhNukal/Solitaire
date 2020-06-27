#v6

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
        x = self.get(index)
        self.contents.pop(index)
        return x
    
    def __len__(self):
        return len(self.contents)
        
class Main_Deck(Deck):
    def __init__(self):
        self.contents = []
        for i in ['heart', 'spade', 'diamd', 'clove']:
            for j in range(1, 14):
                self.contents.append(Card(i, j).flip())
        random.shuffle(self.contents)