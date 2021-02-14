# NOTE
# this class is built according the classic Iterator design pattern
# but is not idiomatic Python, just as a didactic example for iterator

# it's attempting to implement __next__ in Sentence to make it an iterable
# and also an iterator, but it is a very bad idea, and it's a anti-pattern

# An iterable should never act as an iterator over itself. In other words,
# iterables must implement __iter__, but not __next__.
# On the other hand, for convenience, iterators should be iterable.
# An iterator’s __iter__ should just return self.

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    # without this method, the test below can still pass
    # but it can not pass isinstance(x,Iterator) since __next__
    # and __iter__ is what a implementation of iterator is expected
    def __iter__(self):
        return self


if __name__ == '__main__':
    s = Sentence('"The time has come," the Walrus said,')
    print(s)
    for word in s:
        print(word)
    print(list(s))
