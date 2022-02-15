import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        """constructor"""
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        """special method for len()"""
        return len(self._cards)

    def __getitem__(self, position):
        """
        special method for:
        * indexing
        * slicing
        * random.choice()
        * Iterator (call __iter__ first and then call __getitem__)
        """
        return self._cards[position]


def spades_high(card):
    """
    Key function for sorting card
    """
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


beer_card = Card("7", "diamonds")
deck = FrenchDeck()
for card in sorted(deck, key=spades_high):
    print(card)
