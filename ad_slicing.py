# the benefit for that range and slices exclude the last item

l = [1, 2, 3, 4, 5, 6, 7]
print(l[:3])  # produce the exact number of elements which in this case is three
print(l[3:])  # together with the previous line, the list is splited by a single same number 3
print(len(l[2:5]))  # the number of the element of the slicing is stop-start, which here is 5-2=3

# slice can be a object, use it that way can prevent filling your code with hardcoded slices everywhere
invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                     $17.50    3    $52.50
1489  6mm Tactile Switch x20                 $4.95    2     $9.90
1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
"""
SKU = slice(1, 6)
DISCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
# ITEM_TOTAL = slice(55, ...)
line_items = invoice.split('\n')[2:]

for item in line_items:
    print(item[UNIT_PRICE], item[DISCRIPTION])

# multidimensional slicing and Ellipsis.(since built-in sequence types in python are one-dimension, they only support one
# index or slice, not a tuple of them)
# a[i, j]  # used in numpy.ndarray to get a item. python call a.__getitem__((i,j))
# a[m:n, k:l]  # two-dimensional, in numpy

# ... is an alias to Ellipsis Object, which is the single instance for ellipsis class. and as an object, so it can be used
# to pass as an argument to function and a part of slice specification.
# function(...,arg1,arg2) (use as an argument)
#  a[1:...] can be a shortcut for a[1,:,:,:] (one comma, one dimension)

# no Ellipsis or mutipledimensional indexes and slicing


# assigning to slice
l = list(range(0, 11))
print(l)
del l[8:]
print(l)
l[2:5] = [12, 13, 14]
print(l)
# l[1:3]=100 can be done
l[1:3] = [100]  # 1 and 12 is replaced by 100
print(l)
