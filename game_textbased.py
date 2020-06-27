#v2

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
        
        self.distribute_cards()
        
        
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
        
        
    def __repr__(self):
        max_len = 0
        for deck in [self.deck_1, self.deck_2, self.deck_3, self.deck_4, self.deck_5, self.deck_6, self.deck_7]:
            if len(deck) > max_len:
                max_len = len(deck)
        if len(self.discard_pile) == 0:
            discard_1 = '[ Empty ]'
            discard_2 = '[ Empty ]'
            discard_3 = '[ Empty ]'
        elif len(self.discard_pile) == 1:
            discard_1 = f'{str(self.discard_pile.get(-1))}'
            discard_2 = '[ Empty ]'
            discard_3 = '[ Empty ]'
        elif len(self.discard_pile) == 2:
            discard_1 = f'{str(self.discard_pile.get(-1))}'
            discard_2 = f'{str(self.discard_pile.get(-2))}'
            discard_3 = '[ Empty ]'
        else:
            discard_1 = f'{str(self.discard_pile.get(-1))}'
            discard_2 = f'{str(self.discard_pile.get(-2))}'
            discard_3 = f'{str(self.discard_pile.get(-3))}'
        if len(self.foundation_1) == 0:
            found_1 = '[ Empty ]'
        else:
            found_1 = f'{str(self.foundation_1.get(-1))}'
        if len(self.foundation_2) == 0:
            found_2 = '[ Empty ]'
        else:
            found_2 = f'{str(self.foundation_2.get(-1))}'
        if len(self.foundation_3) == 0:
            found_3 = '[ Empty ]'
        else:
            found_3 = f'{str(self.foundation_3.get(-1))}'
        if len(self.foundation_4) == 0:
            found_4 = '[ Empty ]'
        else:
            found_4 = f'{str(self.foundation_4.get(-1))}'
        if len(self.deck_1) == 0:
            d_1 = '[ Empty ]'
        else:
            d_1 = f'{str(self.deck_1.get(0))}'
        if len(self.deck_2) == 0:
            d_2 = '[ Empty ]'
        else:
            d_2 = f'{str(self.deck_2.get(0))}'
        if len(self.deck_3) == 0:
            d_3 = '[ Empty ]'
        else:
            d_3 = f'{str(self.deck_3.get(0))}'
        if len(self.deck_4) == 0:
            d_4 = '[ Empty ]'
        else:
            d_4 = f'{str(self.deck_4.get(0))}'
        if len(self.deck_5) == 0:
            d_5 = '[ Empty ]'
        else:
            d_5 = f'{str(self.deck_5.get(0))}'
        if len(self.deck_6) == 0:
            d_6 = '[ Empty ]'
        else:
            d_6 = f'{str(self.deck_6.get(0))}'
        if len(self.deck_1) == 7:
            d_7 = '[ Empty ]'
        else:
            d_7 = f'{str(self.deck_7.get(1))}'
        line_1 = f'[ Draw  ] {discard_1}           {found_1} {found_2} {found_3} {found_4}'
        line_2 = f'          {discard_2}'
        line_3 = f'          {discard_3}'
        line_4 = f'{d_1} {d_2} {d_3} {d_4} {d_5} {d_6} {d_7}'
        lines_end = []
        for i in range(max_len-1):
            line = ''
            for j in [self.deck_1, self.deck_2, self.deck_3, self.deck_4, self.deck_5, self.deck_6, self.deck_7]:
                if len(j) >= i + 2:
                    line += f'{str(j.get(i+1))} '
                else:
                    line += '          '
            lines_end.append(line)
        lines = [line_1, line_2, line_3, line_4, *lines_end]
        return '\n'.join(lines)