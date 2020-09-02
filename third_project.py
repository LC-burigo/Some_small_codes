from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:

    def __init__(self):
        print("Creating New Ordered Deck")
        self.allcards = [(s, r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.allcards)

    def split_in_half(self):
        return self.allcards[:26], self.allcards[26:]


deck_one = Deck()
deck_one.shuffle()
first_half, second_half = deck_one.split_in_half()
print(first_half)
print(second_half)
