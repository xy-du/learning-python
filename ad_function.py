# first-class function :  functions as first-class objects
# first-class:
# create at runtime
# can be assigned to a variable or element in data structure
# can be passed to a function
# can be returned from a function

def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


# print(factorial(42))
# print(factorial.__doc__)
# print(type(factorial))
#
fact = factorial
# print(fact)
# fact(5)
# print(map(factorial, range(11)))
# print(list(map(fact, range(11))))


# high-order functions:
# receive function as args, return function as result
# eg.  map, filter, reduce, apply
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']


# print(sorted(fruits, key=len))


def reverse(words):
    return words[::-1]


# the origin data is not changed
# print(sorted(fruits, key=reverse))

l1 = list(map(fact, range(6)))
l2 = [fact(n) for n in range(6)]
l3 = list(map(fact, filter(lambda n: n % 2, range(6))))
l4 = [fact(n) for n in range(6) if n % 2]
print(l1)
print(l2)
print(l3)
print(l4)

from functools import reduce
from operator import add

print(reduce(add, range(100)))
print(sum(range(100)))
