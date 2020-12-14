"""this is a docstring"""

def factorial(n):
    """return n!"""
    return 1 if n < 2 else factorial(n - 1) * n

print(factorial(42))
print(factorial.__doc__)
print(type(factorial))

fact=factorial
print(fact(5))
print(map(fact,range(0,11)))
print(list(map(fact,range(0,11))))


# import test
#
# print('here is main.py. __name__ = ',__name__)
# if(__name__=='__main__'):
#     print('test.py is running directly')
# else:
#     print('test.py is running by others')