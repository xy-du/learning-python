# a generator expression can be seen as a lazy version of list comprehension

def gen_AB():
    print('begin')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')


ls = [x * 3 for x in gen_AB()]
print(ls)

ge = (x * 3 for x in gen_AB())
print(ge)
for i in ge:
    print(i)

# you can see that in list comprehension all items are yield at once to
# produce a full list
# but in generator expression, it just produce a generator, and the item
# will be yield one by one on demand
