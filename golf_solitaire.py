from Card import Card
from Deck import Deck


def displayGrid(grid):

    headerStr = ""
    for row in range(7):
        headerStr += " \t" + str(row) + "\t "
    print(headerStr)
    print()

    for row in range(4, -1, -1):
        rowStr = "|\t"
        for col in range(7):
            offset = 5 - len(grid[col])
            rowIdx = row - offset

            if(rowIdx >= 0):
                rowStr += str(grid[col][rowIdx]) + "\t|\t"
            else:
                rowStr += "  \t|\t"
            
        print(rowStr)
        print()



def initGrid(deck):
# this will store full grid
    grid = []

# will need 7 columns
    for col in range(7):
        column = []

# each column gets 5 cards
        for row in range(5):
            card = deck.drawCard()
            column.append(card)
        grid.append(column)

    return grid



# checkWin
def checkWin(grid):
# check columns in grid
    for col in grid:
#if any columns have cards, we aren't done
        if len(col) > 0:
            return False
# if here, everything is empty
    return True

# isPlayable
def isPlayable(card1, card2):
    if card1 is None or card2 is None:
        return True
    
    value1 = card1.getValue()
    value2 = card2.getValue()

    # find the difference between cards
    diff = abs(value1 - value2)

    # check normal or wrap-around match
    if diff == 1:
        return True

    if diff == 12:
        return True

    # not allowed
    return False

# playFromDeck
def playFromDeck(deck):
    if deck.cardsLeft() > 0:
        return deck.drawCard()
    return None

# playCard
def playCard(grid, selectedIndex, waste):

# make sure column exists
    if selectedIndex < 0 or selectedIndex >= len(grid):
        return None

# make sure column not empty
    if len(grid[selectedIndex]) == 0:
        return None

    card = grid[selectedIndex][-1]

# if there is no waste card yet, take it
    if waste is None:
        return grid[selectedIndex].pop()

    if isPlayable(card, waste):
        return grid[selectedIndex].pop()
    
# if here, move is not allowed
    print("Card cannot be played.")
    return None


def main():
# set up deck and grid
    deck = Deck()
    grid = initGrid(deck)
    waste = None

    print("Welcome to Golf Solitaire!")
# keep playing until user quits or wins
    while True:

        # show the current board
        displayGrid(grid)

        # show waste card
        if waste is None:
            print("Waste card: None")
        else:
            print("Waste card:", waste)

        print("Cards left in deck:", deck.cardsLeft())

        # check if the player has won
        if checkWin(grid):
            print("You win the game!")
            break
# ask user what they want to do
        move = input("Type column (0-6), 'd' to draw, or 'q' to quit: ")

        # quit option
        if move == "q" or move == "quit":
            print("Game ended.")
            break
# ask user what they want to do
        move = input("Type column (0-6), 'd' to draw, or 'q' to quit: ")

        # quit option
        if move == "q" or move == "quit":
            print("Game ended.")
            break

if __name__ == "__main__":
    main()