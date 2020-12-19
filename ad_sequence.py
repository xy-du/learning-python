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

# list.sort method sort a list in place, and return None to indicate this.(Return None to show that the original
# list is not changed is a python convention). drawback is that you will not be able to use fluent interface style
# both list.sort and sorted function have two optional, keyword-only arguments, 'key' and 'reversed'
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(fruits)
print(sorted(fruits))
print(sorted(fruits, key=len, reverse=True))
print(sorted(fruits, key=min))
# list sort happened in place.change the original data.
fruits.sort()
print(fruits.sort())  # this one will just return None
print(fruits)
fruits.sort(key=len, reverse=True)
print(fruits)

# manage ordered sequence with bisect
# input(prompt) can accept user's input
# function.__name__   get the name of the function
# {digit:format_specification} digit is the position of the arguments following
# 'separator'.join(iterable)  concatenate all the items with the separator between each one of them
# bisect=bisect_right and bisect_left is only different when the needle is the same with the element they found,
# former will return the index behind it and the latter will return the index right on it (which will make item
# insert just before it if the index is used for insert)
import bisect

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

# msg = input('choose the binary search method:')
# if int(msg) == 0:
#     bisect_fn = bisect.bisect
# else:
#     bisect_fn = bisect.bisect_left

bisect_fn = bisect.bisect

print('use method : ', bisect_fn.__name__)
fmt = '{0:2d} @ {1:2d}     {2}{0:2d}'
print('haystack--> ', ' '.join('%2d' % n for n in HAYSTACK))
for needle in reversed(NEEDLES):
    index = bisect_fn(HAYSTACK, needle)
    offset = index * '  |'
    print(fmt.format(needle, index, offset))


# a interesting application is using bisect to perform table look up


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


ls = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
print(ls)

import random

ls_size = 7
random.seed(1729)
my_ls = []
for i in range(ls_size):
    new_item = random.randrange(ls_size * 2)
    bisect.insort(my_ls, new_item)
    print('%2d-->' % new_item, my_ls)

# list is very handy, but do not overuse it, under certain circumstances, other choices are much more efficient
# if you want to store 10 million float number, use array would be wise
# array will not store the full-fledged float object, but only the packed bytes representing their machine value
# just like in C language
# this will save memory for large sequence
# array will not let you put in any number that does not match its type (yeah, array has its type)
import array

# 'd' stands for double float, here you set its type
# the tofile and fromfile function is much more faster than read or write number from txt file, which involves in
# parsing every line with the float() built-in function
f_arr1 = array.array('d', (random.random() for i in range(10 ** 7)))
print(f_arr1[-1])
fp = open('floats.bin', 'wb')  # wb : write, binary
f_arr1.tofile(fp)
fp.close()
f_arr2 = array.array('d')
fp = open('floats.bin', 'rb')  # rb : read, binary
f_arr2.fromfile(fp, 10 ** 7)
fp.close()
print(f_arr2[-1])
print(f_arr2[-1] == f_arr1[-1])
