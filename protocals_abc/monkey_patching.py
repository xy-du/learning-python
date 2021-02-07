# monkey_patching: change a class or module at runtime without touching its source code
# it is powerful, but the code that does the actual patching is very tightly
# coupled with the program to be patched, often handling private and undocumented parts.

# what shuffle can do
from random import shuffle

l = [1, 2, 3]
shuffle(l)
print(l)

from sequence_hack.protocol_ducktyping import FrenchDeck

fd = FrenchDeck()

# TypeError: 'FrenchDeck' object does not support item assignment
# shuffle(fd)

# The problem is that shuffle operates by swapping items inside the
# collection, and FrenchDeck only implements the immutable sequence protocol.
# Mutable sequences must also provide a __setitem__ method.

######################################################
# RUN the following in python console
######################################################

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck2:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

# deck = FrenchDeck2()
# from random import shuffle
#
# shuffle(deck)  # TypeError: 'FrenchDeck2' object does not support item assignment
# FrenchDeck2.__setitem__ = set_card
# shuffle(deck)

# we add the __setitem__ method for the class at runtime, this is monkey-patch,
# and we can see, you have to know the inside of the class well, so it's pretty tightly coupled

# FrenchDeck only implements the immutable sequence protocol.
# Mutable sequences must also provide a __setitem__ method.

# this example highlights that protocols are dynamic: random.shuffle doesn't care what
# type of argument it gets, it only needs the object to implement part of
# the mutable sequence protocol. It doesn't even matter if the object was
# “born” with the necessary methods or if they were somehow acquired later.
