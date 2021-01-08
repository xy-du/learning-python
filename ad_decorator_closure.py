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
target()
