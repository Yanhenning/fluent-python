import collections
from typing import List

suits_values = dict(clubs=3, hearts=2, spades=1, diamonds=0)

# O livro utiliza o namedtuple para criar o card, aqui eu decedi utilizar uma classe para fazer essas comparações das cartas

CardType = collections.namedtuple('Card', ['rank', 'suit'])


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __lt__(self, other):
        if self.rank < other.rank:
            return True
        if self.rank == other.rank and suits_values[self.suit] < suits_values[other.suit]:
            return True
        return False

    def __gt__(self, other):
        if self.rank > other.rank:
            return True
        return self.rank == other.rank and suits_values[self.suit] > suits_values[other.suit]

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __ne__(self, other):
        return self.rank != other.rank or self.suit != other.suit

    def __repr__(self):
        return f'Card: {self.rank} {self.suit}'


class FrenchDeck:
    ranks: List[str] = [str(n) for n in range(2, 11)] + list('JQKA')
    suits: List[str] = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
