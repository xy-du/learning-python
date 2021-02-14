# A sentence class that implement a sequence protocol which include __getitem__ and __len__

# the __getitem__ in it make itself iterable, and that why sequence type is iterable


# when the interpreter needs to iterate over and object x, it automatically call iter(x), then:
#   1. Checks whether the object implements __iter__, and calls that to obtain an iterator.
#   2. If __iter__ is not implemented, but __getitem__ is implemented, Python creates
#       an iterator that attempts to fetch items in order, starting from index 0 (zero).
#   3. If that fails, Python raises TypeError, usually saying “C object is not iterable,” where
#       C is the class of the target object.
# NOTE:
# this is the extreme form of duck typing: an object is considered iterable
# not only when it implements the special method, __iter__, but also when
# it implements __getitem__, as long as __getitem__ accepts int keys starting from 0.
# see the goose-type approach below


import re
import reprlib
from collections import abc

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, item):
        return self.words[item]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)  # repr limit the generated string to 30 characters


# in the goose-type approach, the definition for iterable is simpler but not flexible:
# an object is considered iterable if it implements the __iter__ method.
# No subclassing or registration is required, because abc.Iterable
# implements the __subclasshook__

class Foo:
    def __iter__(self):
        pass

# NOTE:
# the most accurate way to check whether an object x is iterable is to call
# iter(x) and handle the TypeError exception instead of isinstance(x,abc.Iterable),
# because iter(x) also consider the __getitem__, while the Iterable ABC does not


if __name__ == '__main__':
    s = Sentence('"The time has come," the Walrus said,')
    print(s)
    print(len(s))
    for word in s:  # the __getitem__ is why sentence can be iterable
        print(word)

    print('iterable test in goose-typing approach')
    f = Foo()
    print(isinstance(f, abc.Iterable))
