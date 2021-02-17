def vowel(c):
    return c.lower() in 'aeiou'


print(list(filter(vowel, 'Aardvark')))

import itertools

print(list(itertools.filterfalse(vowel, 'Aardvark')))
print(list(itertools.dropwhile(vowel, 'Aardvark')))  # return from the first false, no further check
print(list(itertools.takewhile(vowel, 'Aardvark')))  # return from the first false, no further check
print(list(itertools.compress('Aardvark', (1, 0, 1, 0, 1))))  # missing part will be seen as false
print(list(itertools.islice('Aardvark', 4)))  # just like s[:] except this operation is lazy
print(list(itertools.islice('Aardvark', 1, 4)))
print(list(itertools.islice('Aardvark', 1, 4, 2)))

print("########################")

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
print(list(itertools.accumulate(sample)))
print(list(itertools.accumulate(sample, max)))
print(list(itertools.accumulate(sample, min)))

import operator

print(list(itertools.accumulate(sample, operator.mul)))
print(list(itertools.accumulate(range(1, 11), operator.mul)))

print(list(map(operator.mul, range(1, 10), range(1, 10))))
print(list(map(operator.mul, range(1, 10), [2, 3, 4])))
print(list(map(lambda a, b: (a, b), range(1, 10), [2, 3, 4])))
print(list(itertools.starmap(operator.mul, enumerate('abcdefg', 1))))

print(list(enumerate('abcdefg', 1)))

print("########################")

print(list(itertools.chain('ABC', range(2))))
print(list(itertools.chain(enumerate('ABC'))))
print(list(itertools.chain.from_iterable(enumerate('ABC'))))
print(list(zip('ABC', range(5))))
print(list(zip('ABC', range(5), [10, 20, 30, 40])))
print(list(itertools.zip_longest('ABC', range(5), [10, 20, 30, 40])))
print(list(itertools.zip_longest('ABC', range(5), [10, 20, 30, 40], fillvalue='?')))

print("########################")
print(list(itertools.product('ABC', range(2))))
suits = 'spades hearts diamonds suits'.split()
print(list(itertools.product('AK', suits)))
print(list(itertools.product('ABC')))
print(list(itertools.product('ABC', repeat=2)))  # repeate is like the number of the layer of loops
print(list(itertools.product('AB', range(2), repeat=2)))

print("########################")
ct = itertools.count()
print(next(ct))
print(next(ct))
print(list(itertools.islice(itertools.count(1, .3), 3)))
cy = itertools.cycle('AB')
print(next(cy))
print(next(cy))
print(next(cy))
print(list(itertools.islice(cy, 7)))
rp = itertools.repeat(7)
print(next(rp))
print(next(rp))
print(list(itertools.repeat(8, 4)))
print(list(map(operator.mul, range(10), itertools.repeat(5))))

print("########################")
print(list(itertools.combinations('ABC', 2)))
print(list(itertools.combinations_with_replacement('ABC', 2)))
print(list(itertools.permutations('ABC', 2)))
print(list(itertools.product('ABC', repeat=2)))

print("########################")
print(list(itertools.groupby('AAABBBBCCCCCDDDDDDD')))
for c, group in itertools.groupby('AAABBBBCCCCCDDDDDDD'):
    print(c, '---->', list(group))
animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']
# groupby iterates sequentially, so sort it first to make items of same length are together
animals = sorted(animals, key=len)
print(animals)
for length, gruop in itertools.groupby(animals, len):
    print(length, '--->', list(gruop))
print(list(reversed(animals)))
for length, gruop in itertools.groupby(reversed(animals), len):
    print(length, '--->', list(gruop))

print("########################")
g1, g2 = itertools.tee('ABC')
# print(list(g1)) # do built a list using the generator yet since it will consume all the items
# print(list(g2))

print(next(g1))
print(next(g1))
print(next(g2))

print(list(g1))
print(list(g2))
