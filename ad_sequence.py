"""
built-in sequences
    container sequences:
        list, tuple, cellections.deque.   they can hold difference type
    flat sequences:
        str, bytes, betearray, memoryview, array.array.   hold items of one type.

OR group by:
    mutable:
        list, array.array, bytearray, collections.deque, memoryview
    immutable:
        tuple, str, bytes
"""

"""
list comprehensions(listcomps): quick way to build a sequence of list
generator expression(genexps): a way to build sequences of other kinds
"""

symbols = '$¢£¥€¤'
codes = []
for s in symbols:
    codes.append(ord(s))
print(codes)

# apparently this way is more concise
# listcomps is meants to do one thing: build list
# python ignore the line breaks in [] {} and (), so you can do multiple line listcomps
codes = [ord(s) for s in symbols]
print(codes)

# in python2 the x used in listcomps will leak, i.e. it will affect the value surrounding it.
# but this is fixed in python3, where variables in listcomps will just be a local var
x = 'a'
lx = [x for x in 'ABC']
print(x)
print(lx)

# same list can be obtained with listcomps without the contortion of the lambda, map, filter
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)
beyond_ascii = list(filter(lambda x: x > 127, map(ord, symbols)))
print(beyond_ascii)

# cartesien product
# imagine a kind of T-shirt has two size and three color
# pay attention to the order of the var appearing in the listcomps
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
shirt_ls = [(color, size)
            for color in colors
            for size in sizes]
print(shirt_ls)
for color in colors:
    for size in sizes:
        print((color, size))
