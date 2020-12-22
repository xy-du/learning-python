# set theory
# set and frozenset become built-ins in python 2.6
# set elements must be hashable.
# set is not hashable but frozenset is, which make it can be the element of set

# the most significant character of set it the unique elements, which can be used to remove duplication
l = ['spam', 'spam', 'egg', 'spam']
s = set(l)  # build set from list
print(s)
ls = list(s)  # build list from set
print(ls)
s1 = {1, 2, 3}  # normal way to build a set
print(type(s1))

# infix operator of set
# a | b   union
# a & b    intersection
# a - b  difference
# use these infix operator well can save you a lots of work
# example : find 'needle'(few elements) in 'haystack'(a lot of elements)
needle = {11, 2, 3}
haystack = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(needle & haystack)
# which is lots better than double loops
# but what you have can not always be set, but you can always built them on the fly
# of course there will be case to build the set, but if either one of the set is set already, it will be worth it
nd = [11, 2, 3]
hs = [2, 3, 4, 5, 6, 7, 8, 9]
print(set(nd) & set(hs))
print(set(nd).intersection(hs))
