import time
from clockdeco import clock


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


# so that if you import this file, this part will not get executed
if __name__ == '__main__':
    print('*' * 40, 'snooze(.123)')
    snooze(.123)
    print('*' * 40, 'factorial(6)')
    factorial(6)

# the factorial actually hold the reference to the inner function clocked of clock
# and also, the factorial's attribute has been masked. this probably is not what you want at a certain time
print(factorial.__name__)

# This is the typical behavior of a decorator: it replaces the decorated function with a new function that
# accepts the same arguments and (usually) returns whatever the decorated function was supposed to return,
# while also doing some extra processing.

# shortcomings of the clock decorator:
#   attributes of decorated function are masked, like __name__ __doc__
#   it does not support keyword arguments
# revised version: see clockdeco2.py in this direcotory
