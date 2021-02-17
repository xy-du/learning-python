# Nested for loops are the traditional solution when a
# generator function needs to yield values produced from another generator.

def chain_v1(*iterable):
    for it in iterable:
        for i in it:
            yield i


# but with yield from since python 3.4, things have changed
def chain_v2(*iterable):
    for it in iterable:
        yield from it


l = [1, 2, 3]
s = 'ABC'
print(list(chain_v1(l, s)))
print(list(chain_v2(l, s)))
