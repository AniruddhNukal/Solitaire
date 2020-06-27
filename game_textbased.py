#v1

from deck import Deck, Main_Deck

class Game:
    def __init__(self):
        self.draw_pile = Main_Deck()
        self.discard_pile = Deck()
        self.foundation_1 = Deck()
        self.foundation_2 = Deck()
        self.foundation_3 = Deck()
        self.foundation_4 = Deck()
        
        self.deck_1 = Deck()
        self.deck_2 = Deck()
        self.deck_3 = Deck()
        self.deck_4 = Deck()
        self.deck_5 = Deck()
        self.deck_6 = Deck()
        self.deck_7 = Deck()
        
        
    def distribute_cards(self):
        self.deck_1.add(self.draw_pile.getremove(0).flip())
        
        self.deck_2.add(self.draw_pile.getremove(0))
        self.deck_2.add(self.draw_pile.getremove(0).flip())
        
        for i in range(2):
            self.deck_3.add(self.draw_pile.getremove(0))
        self.deck_3.add(self.draw_pile.getremove(0).flip())
        
        for i in range(3):
            self.deck_4.add(self.draw_pile.getremove(0))
        self.deck_4.add(self.draw_pile.getremove(0).flip())
        
        for i in range(4):
            self.deck_5.add(self.draw_pile.getremove(0))
        self.deck_5.add(self.draw_pile.getremove(0).flip())
        
        for i in range(5):
            self.deck_6.add(self.draw_pile.getremove(0))
        self.deck_6.add(self.draw_pile.getremove(0).flip())
        
        for i in range(6):
            self.deck_7.add(self.draw_pile.getremove(0))
        self.deck_7.add(self.draw_pile.getremove(0).flip())
        