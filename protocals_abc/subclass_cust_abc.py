import random

from protocals_abc.define_abc import Tombola


class BingoCage(Tombola):
    def __init__(self, items):
        self._items = []
        self._randomizer = random.SystemRandom()
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    # raise the IndexError is what the ABC interface required
    def pick(self):
        try:
            self._items.pop()
        except IndexError:
            raise IndexError('pick for empty BingoCage')

    def __call__(self, *args, **kwargs):
        self.pick()


# we can be lazy and just inherit the suboptimal concrete methods from an ABC,
# (the loaded and inspect methods here)
# The methods inherited from Tombola are not as fast as they could be for BingoCage,
# but they do provide correct results for any Tombola subclass that correctly implements pick and load.

class LotteryBlower(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            return self._balls.pop()
        except ValueError:
            raise LookupError('pick from empty BingoCage')

    # we overwrite the concrete methods in ABCsw with a more efficient way
    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))

# in __init__, self._balls stores list(iterable) and not just a reference to iterable
# (i.e., we did not merely assign iterable to self._balls). this makes LotteryBlower
# flexible because the iterable argument may be any iterable type. At the same time,
# we make sure to store its items in a list so we can pop items.
# And even if we always get lists as the iterable argument, list(iterable) produces
# a copy of the argument, which is a good practice considering we will change the content(pop)
