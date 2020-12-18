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

# generator expression: it yields items one by one. So no whole list in the memory

# initial a tuple and array using genexps. listcomp use brackets but genexps use parentheses
symbols = '$¢£¥€¤'
tp = tuple(ord(s) for s in symbols)  # if it's only one args, no parentheses needed
print(tp)
import array

arr = array.array('I', (ord(s) for s in symbols))  # if it's not the only args, parentheses is mandatory
print(arr)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
# a whole list of t-shirts is never produced
for tshirt in ('%s %s' % (color, size)
               for color in colors
               for size in sizes):
    print(tshirt)

# * and + create new object, and never change their operands
l = [1, 2, 3]
print(l * 2)
print(5 * 'abcd')

# using []*n, whatever in that [], just duplicate them n times
# it's not like, duplicate [] as a whole n times and then put another[] around it
l1 = ['_']
print(l1 * 3)

l2 = ['_', '_', '_']
l = l2 * 3
print(l)
l[0] = 'X'
print(l)

# when [] contains mutable items, like here a list. The reference get duplicate three times, so change one item in one
# list, all the items in the same position in other list alse changed since the refer to the same object.
l3 = [['_', '_', '_']]
l = l3 * 3
print(l)
l[0][1] = 'X'
print(l)
# right way to do it, we need to avoid using * with [] that contains mutable items.

# augmented assignment with sequence
# using += as example, but *= is the same
# a+=b
# for mutable sequence, __iadd__ will make a change in place. But if a doesn't implement __iadd__, s+= will just
# be like a=a+b, valued on the right evaluated first, produce a new object, then it's assigned to a.
# l is a mutable list
l = [1, 2, 3]
print(id(l))
l *= 2
print(id(l))
# l is an immutable tuple
l = (1, 2, 3)
print(id(l))
l *= 2
print(id(l))

# do the try-catch block so that the program will continue, so print(t) will show us the 'corner case'
t = (1, 2, [3, 4])
try:
    t[2] += [7, 9]
except TypeError as e:
    print('there is an error: ' + str(e))
    pass
print(t)
