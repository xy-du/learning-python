# if you want a sequence type, you don't have to inherit from any special class to create a fully functional
# you just need to implement the method that fulfill the sequence protocol.
# protocol is an informal interface, defined only in the documents and not in the code.
# for sequence protocol, it just entails the __len__ and __getitem__
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

# when a  python coder see this class, they should understand that it's a sequence type, even if it subclasses object
# NOTE:
# we say it's a sequence type because it behavior like one, and that is what matters, and this is known as
# ducking typing

# protocols are informal and unforced, you can get away with implementing just part of a protocal
# if you know the specific context where a class will be used. For example, to support iteration,
# only __getitem__ is required; there is no need to provide __len__.
