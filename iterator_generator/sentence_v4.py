# lazy evaluation and eager evaluation are actual technical terms
# in programming language theory


# Sentence in sentence_v3 is not lazy since in __init__, it eagerly builds a
# list of all words in the text
# this is not good if the text is tremendous long since it will occupy a lot memory,
# and it's also a huge waste if you only need the first several words


# Whenever you are using Python 3 and start wondering
# “Is there a lazy way of doing this?”, often the answer is “Yes.”

# The re.finditer function is a lazy version of re.findall which,
# instead of a list, returns a generator producing re.MatchObject instances on demand.
# If there are many matches, re.finditer saves a lot of memory. Using it,
# our third version of Sentence is now lazy: it only produces the next word when it is needed.

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for w in RE_WORD.finditer(self.text):
            yield w.group()
        return


if __name__ == '__main__':
    s = Sentence('"The time has come," the Walrus said,')
    print(s)
    for word in s:
        print(word)
    print(list(s))
