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
# print(l1)
# print(l2)
# print(l3)
# print(l4)

from functools import reduce
from operator import add

# print(reduce(add, range(100)))
# print(sum(range(100)))

# lambda is used to create an anonymous function
# pure expression.  can not make assignment or use any other Python statement such as while,try,etc
# the best use of anonymous functions is in the context of an argument list.
# outsize the arguments to higher-order functions, anonymous functions are rarely useful in Python
# print(sorted(fruits, key=lambda word: word[::-1]))

# seven callable objects in python
# built-in function.  len  time.shrftime
# built-in method   dict.get
# user-defined functions
# method.   functions defined in the body of a class
# class.   __new__   __init__   then return new object to caller
# class instances.   if a class implements __call__  method. its instance can be invoked as a function
# generator function.    method or function using the yield keywords to return a generator

# the safiest way to determine if an object is callable is use the callable() built-in:
# print([callable(obj) for obj in (abs, str, 123)])


# not only Python function can be object, object can be made to behave like function.
# implement a __call__ instance method is all it takes
import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self, *args, **kwargs):
        return self.pick()


bingo = BingoCage(range(3))
# print(bingo.pick())
# print(bingo())
# print(callable(bingo))


# function object has many attributes beyond __doc__, see below
print(dir(factorial))


# like the instances of user-defined class, function use __dict__ to store its attributes
# assign arbitrary attribute to functions is not a common prctice in general, but it can be done, and Django use
# this a lot
# we put our attentio to the attributes that is specific to functions and not in the general classes
# eg. __code__ __defaults__  __annotations__ in this 'special set' will be used by IDEs and framework
class C:
    pass


def func():
    pass


obj = C()
print(set(dir(func)) - set(dir(obj)))
