# coroutine has yield in it, but it is more complicate than a simple generator function.
# key info:
# next(), send(), throw(), yield from, it can return value

# there four state of a coroutine:
# GEN_CREATED  GEN_RUNNING  GEN_SUSPENDED  GEN_CLOSED
# see the example below to see when the coroutine in on one of these stage


def simple_coro(a):
    print('started a:', a)
    b = yield a
    print('received b:', b)
    c = yield b + a
    print('received c:', c)


def simple_coro_1():
    print('begin')
    a = yield  # when there is nothing behind yield,it yield 'None', and now it's more like a controller
    print('end a=', a)


import inspect

# after the coroutine is created, no code in it will be ran，
# run a next() or .send(None) on it will cause the code advances to the
# first yield line, (this process is called priming the coroutine)
# it will stop precisely at the word 'yield', for now, it's just like
# a normal generator, coroutine will be suspended now and the control is
# handed over to the caller,
# take 'b = yield a' for example
# after the first next() or send(None) on the coroutine, the value of a will
# be yielded to the caller, and the code stops until the caller invoke .send(arg)
# on it in the feature, and when that happens, the 'arg' will be assigned to the
# variable on the left of the yield line, b in this example, and the code advanced
# to the next yield line following the code logic.

# NOTE:
# In coroutine, the yield keyword can be used in the expression, which is not the
# case for normal generator

if __name__ == '__main__':
    co1 = simple_coro_1()
    print(next(co1))
    try:
        co1.send(23)
    except StopIteration:
        print('catch StopIteration, coroutine finished')

    print('********************')

    co = simple_coro(1)
    print(inspect.getgeneratorstate(co))
    print(next(co))  # using .send(None) can also do the priming
    # print(co.send(None))
    print(inspect.getgeneratorstate(co))
    print(co.send(2))
    print(inspect.getgeneratorstate(co))
    try:
        print(co.send(3))  # when the coroutine is finished, a StopIteration exception is raised
    except StopIteration:
        print('the coroutine is finished now, the states of it now it:')
        print(inspect.getgeneratorstate(co))
