import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [
            Card(rank, suit) for suit in self.suits for rank in self.ranks
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def spades_high(self, card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(self.suit_values) + self.suit_values[card.suit]


deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(Card('Q', 'hearts') in deck)
for card in deck:
    print(card)

for card in sorted(deck, key=deck.spades_high):
    print(card)

print(deck.suit_values)