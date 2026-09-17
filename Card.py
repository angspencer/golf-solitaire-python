class Card:
# this creates a card with a suit and value
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

# returns the suit of the card
    def getSuit(self):
        return self.suit

# returns the number value of the card
    def getValue(self):
        return self.value

# prints the card
    def __str__(self):
        return str(self.value) + self.suit