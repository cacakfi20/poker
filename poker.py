import random

class Card:
    """
    Class that represents a card.
    """

    def __init__(self, _val, _col):
        self.val = _val
        self.col = _col

    def print_card(self):
        print(f"{self.val}{self.col}")

    def return_card(self):
        return [self.val, self.col]


class Deck:
    """
    Class that represents a deck.
    """

    def __init__(self):
        self.__cards = []
        colors = ["♥", "♦", "♠", "♣"]
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

        for color in colors:
            for value in values:
                self.__cards.append(Card(value, color))

    def shuffle(self):
        random.shuffle(self.__cards)

    def draw_card(self):
        return self.__cards.pop()

class Player:
    """
    Class that represents a player.
    """

    def __init__(self, _name, _money):
        self.name = _name
        self.money = _money
        self.__hand = []

    def draw(self, number, deck):
        for i in range(number):
            self.__hand.append(deck.draw_card())

    def print_hand(self):
        colors = []
        values = []
        for card in self.__hand:
            colors.append(card.col)
            values.append(card.val)
        if values[0] == 10 or values[1] == 10:
            if values[0] == 10 and values[1] != 10:
                print("┌─────────┐ ┌─────────┐")
                print(f"│.{values[0]}. . . │ │.{values[1]}. . . .│")
                print("│. . . . .│ │. . . . .│")
                print(f"│. . {colors[0]} . .│ │. . {colors[1]} . .│")
                print("│. . . . .│ │. . . . .│")
                print(f"│ . . .{values[0]}.│ │. . . .{values[1]}.│")
                print("└─────────┘ └─────────┘")
            if values[1] == 10 and values[0] != 10:
                print("┌─────────┐ ┌─────────┐")
                print(f"│.{values[0]}. . . .│ │.{values[1]}. . . │")
                print("│. . . . .│ │. . . . .│")
                print(f"│. . {colors[0]} . .│ │. . {colors[1]} . .│")
                print("│. . . . .│ │. . . . .│")
                print(f"│. . . .{values[0]}. │ . . .{values[1]}.│")
                print("└─────────┘ └─────────┘")
            if values[1] == 10 and values[0] == 10:
                print("┌─────────┐ ┌─────────┐")
                print(f"│.{values[0]}. . . │ │.{values[1]}. . . │")
                print("│. . . . .│ │. . . . .│")
                print(f"│. . {colors[0]} . .│ │. . {colors[1]} . .│")
                print("│. . . . .│ │. . . . .│")
                print(f"│ . . .{values[0]}.│ │ . . .{values[1]}.│")
                print("└─────────┘ └─────────┘")
        else:
            print("┌─────────┐ ┌─────────┐")
            print(f"│.{values[0]}. . . .│ │.{values[1]}. . . .│")
            print("│. . . . .│ │. . . . .│")
            print(f"│. . {colors[0]} . .│ │. . {colors[1]} . .│")
            print("│. . . . .│ │. . . . .│")
            print(f"│. . . .{values[0]}.│ │. . . .{values[1]}.│")
            print("└─────────┘ └─────────┘")

class Game:
    """
    Class that represents a game.
    """
    def __init__(self, _pot, _min):
        self.pot = _pot
        self.min = _min
        self.cards = []

    def card_turn(self, number, deck):
        for i in range(number):
            self.cards.append(deck.draw_card())

deck = Deck()
deck.shuffle()

p1 = Player('Filip', 1000)
p1.draw(2, deck)
p1.print_hand()
