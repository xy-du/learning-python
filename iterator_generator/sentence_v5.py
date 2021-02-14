# the only difference here is the __iter__ method
# it no longer a generator function since there is no yield in it
# but it still produce a generator using a generator expression

# genexps can always be replaced by generator function, but sometimes
# are more convenient

# how to choose between generator function and genexps
# a generator expression is a syntactic shortcut to create a generator
# without defining and calling a function. On the other hand, generator functions
# are much more flexible: you can code complex logic with multiple
# statements, and can even use them as coroutines
# generator function has name so it can be reused, even you can assign a name to
# genexps, but that is stretching its intended usage as a one-off generator.

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (w.group() for w in RE_WORD.finditer(self.text))


if __name__ == '__main__':
    s = Sentence('"The time has come," the Walrus said,')
    print(s)
    for word in s:
        print(word)
    print(list(s))
