class DemoException(Exception):
    """An exception type for the demonstration"""


def excp_handling():
    print('start')
    while True:
        try:
            x = yield
        except DemoException:
            print('catch DemoException')
        else:
            print('coroutine received x=', x)
    raise RuntimeError('this line should never run')


co = excp_handling()
next(co)
co.send(1)
co.send(2)
co.throw(DemoException)  # if the exception is handled, it just run to the next yield line
co.send(3)  # since the exception is caught in generator, it still works
try:
    co.throw(RuntimeError)  # if it's not handed in the coroutine, it will propagate to caller(here)
except RuntimeError:
    print('caller catch the run time error')
# co.send(4) # this cause StopIteration, indicate the co has been terminate

print('##################')
co = excp_handling()
next(co)
co.send(11)
co.send(22)
co.close()  # close() cause GeneratorExit error,it won't propagate to caller even it's not handled


# co.send(33)


def excp_handling_1():
    print('start')
    while True:
        try:
            x = yield
        except DemoException:
            print('catch DemoException')
        except GeneratorExit:
            print('.close() cause the GeneratorExit')
            break
        else:
            print('coroutine received x=', x)
    print('the catching-GeneratorExit coroutine has ended')


print('##################')
co = excp_handling_1()
next(co)
co.send(11)
co.send(22)
co.close()  # close() cause GeneratorExit error, and it can be caught


# co.send(33)

def excp_handling_2():
    print('start')
    while True:
        try:
            x = yield
        except DemoException:
            print('catch DemoException')
        except GeneratorExit:
            break
        else:
            print('coroutine received x=', x)
    print('the catching-GeneratorExit coroutine has ended')


print('##################')
co = excp_handling_2()
next(co)
co.send(111)
co.send(222)
# # close() cause GeneratorExit error, and it cause the finish of the generator
# and the StopIteration with the finish of a generator will not be passed to the
# caller here, this is not the case when the finish is caused by the normal next()
# call on the generator where the StopIteration will be propagate to the caller here
co.close()
# co.send(33)
