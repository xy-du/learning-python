import collections

# this creates a simple class. since python2.6
Card = collections.namedtuple('Card', ['rank', 'suit'])


# a collection class that contains a mount of simple class Card
class FrenchCard:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._card = [Card(rank, suit)
                      for suit in self.suits
                      for rank in self.ranks]

    def __len__(self):
        """
        __XXX__ these are special method
        response to len() standard function
        using things like __len__ and __item__
        you don't have to remember the standard function name. length() or size() or len()???
        you can leverage the standard rich python library and avoid reinvent wheels like random.choice function
        """
        return len(self._card)

    def __getitem__(self, item):
        """response to [] operator"""
        return self._card[item]


# beer_card = Card('7', 'diamonds')
# print(beer_card)

deck = FrenchCard()
print(len(deck))

# print(deck[0])
# print(deck[-1])
# print(deck[1].rank, ' ', deck[1].suit)

# slicing
# print(deck[:3])
# print(deck[12::13])  # get all the suits for rank 'A'

# # iterable
# for card in deck:
#     print(card)
#
# # reverse
# for card in reversed(deck):
#     print(card)

# random choice
# from random import choice
# print(choice(deck))

# 'in' works using a sequential scan, since this class is iterable because of the __getitem__
# print(Card('A','spades') in deck)
# print(Card('7','beasts') in deck)

# sorting
# suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)
#
#
# def spades_high(card):
#     rank_value = FrenchCard.ranks.index(card.rank)
#     return rank_value * len(suit_value) + suit_value[card.suit];
#
#
# # sort in an increasing order
# for card in sorted(deck, key=spades_high):
#     print(card)
