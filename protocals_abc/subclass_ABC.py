# take abc.MutableSequence as a example
# the abstract method in it are:
# __getitem__, __setitem__, __delitem__, __len__, insert

from collections import namedtuple
from collections.abc import MutableSequence

Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck2(MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __len__(self):
        return len(self._cards)

    def __delitem__(self, key):
        del self._cards[key]

    def insert(self, position, value):
        self._cards.insert(position, value)


# you must implement __delitem__ and insert, even if our FrenchDeck2 examples
# do not need those behaviors: the MutableSequence ABC demands them.

# if you comment any method in the class, there will be error here
# say that you comment __delitem__ and insert, the error will be following:
# TypeError: Can't instantiate abstract class FrenchDeck2 with abstract methods __delitem__, insert
# NOTE:
# python do not check the implementation of the abstract method at import time, but only at runtime
# when you actually try to instantiate the class
f = FrenchDeck2()

# NOTE:
#   you have to implement the abstract method in MutableSequence
#   MutableSequence inherit Sequence, and FrenchCard class here inherit many
# ready-to-use concrete methods from these methods
#   you can overwrite the method from ABCs with more efficient implementations
