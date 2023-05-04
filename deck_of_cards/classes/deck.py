from . import card
import random

class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()

    def deal_hands(self):
        new_deck = Deck()
        player_deck = []
        cpu_deck = []
        max_num = 51
        for i in range(26):
            player_deck.append(new_deck.cards.pop(random.randint(0,max_num)))
            max_num -= 1
            cpu_deck.append(new_deck.cards.pop(random.randint(0,max_num)))
            max_num -= 1
        # for card in new_deck.cards:
        #     deck_num = random.randint(0,1)
        #     if len(player_deck) >= 26:
        #         cpu_deck.append(card)
        #     elif len(cpu_deck) >= 26:
        #         player_deck.append(card)
        #     else:
        #         if deck_num:
        #             player_deck.append(card)
        #         else:
        #             cpu_deck.append(card)
        return [player_deck, cpu_deck]