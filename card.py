class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.hidden = False
        
        if self.value == 1:
            self.face = 'A'
        elif self.value == 11:
            self.face = 'J'
        elif self.value == 12:
            self.face = 'Q'
        elif self.value == 13:
            self.face = 'K'
        else:
            self.face = str(self.value)
            
    def __repr__(self):
        if self.hidden:
            return '[card hidden]'
        else:
            return f'[{self.suit} {self.value}]'