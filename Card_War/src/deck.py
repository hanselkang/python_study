# 52 card objects
# Hold as a list of card objects

# Random library shuffle() function

# Pop method from cards list
from card import *


class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


new_deck = Deck()
new_deck.shuffle()
mycard = new_deck.deal_one()
print(mycard)

for card_object in new_deck.all_cards:
    print(card_object)

