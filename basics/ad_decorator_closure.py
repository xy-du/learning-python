# python support class decorator and function decorator, here we talk about the latter
# a decorator is a callable that takes another function as arguments(decorated function), it performs some process
# with the decorated function and return it or replaces it with another function or callable object

def deco(func):
    def inner():
        print('here is the inner function in deco')

    return inner


@deco
def target():
    print('here is the target function')


# this will actually run the inner function in the deco
# target()

register = []


# a real decorator normally will not return the same function but a new inner function. But return a same one
# can indeed happen in same framework where the decorator are used for, say, register.
# see also the test.py and understand the invoke time for decorated function
# and that highlights the difference between 'import time' and 'runtime'
def decorator(func):
    print('decrate function at', func)
    register.append(func)
    return func


# after this function is defined, the decorated function is invoked immediately
@decorator
def func1():
    print('this is func1')


@decorator
def func2():
    print('this is func2')


# this normal function is invoked when it's called
def func3():
    print('this is func3')


def main():
    print(register)  # you will see the func1 and func2 has already append into this list
    func1()  # three normal function invoke
    func2()
    func3()


if __name__ == '__main__':
    main()
