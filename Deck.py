import random
from Card import Card

class Deck:

    def __init__(self):
# create empty deck list
        self.deck = []

# generate and shuffle the deck
        self.generateDeck()
        self.shuffle()

# creates all 52 cards
    def generateDeck(self):
        suits = ["♠", "♣", "♥", "♦"]
        
        for suit in suits:
            for value in range(1, 14):
                self.deck.append(Card(suit, value))

# shuffles the deck by swapping random cards
    def shuffle(self):
        for cards in range(150):
            index1 = random.randint(0, len(self.deck) - 1)
            index2 = random.randint(0, len(self.deck) - 1)

            temp = self.deck[index1]
            self.deck[index1] = self.deck[index2]
            self.deck[index2] = temp

# removes and returns the top card
    def drawCard(self):
        if len(self.deck) > 0:
            return self.deck.pop(0)
        return None

# removes and returns the top card
    def cardsLeft(self):
        return len(self.deck)