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
# fact = factorial
# print(fact)
# fact(5)
# print(map(factorial, range(11)))
# print(list(map(fact, range(11))))


# high-order functions:
# receive function as args, return function as result
# eg.  map, filter, reduce, apply
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))


def reverse(words):
    return words[::-1]


# the origin data is not changed
print(sorted(fruits, key=reverse))
