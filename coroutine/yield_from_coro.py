# delegating generator
# The generator function that contains the yield from <iterable> expression.
# subgenerator
# The generator obtained from the <iterable> part of the yield from expression.
# caller
# PEP 380 uses the term “caller” to refer to the client code that calls the
# delegating generator. Depending on context, you can also use “client” instead
# of “caller,” to distinguish from the delegating generator, which is also a
# “caller” (it calls the subgenerator).

# caller <---> gen <---> subgen
# when a generator gen calls yield from subgen(), the subgen takes over and
# will yield values to the caller of gen; the caller will in effect drive
# subgen directly. Meanwhile gen will be blocked, waiting until subgen terminates
# the gen (delegating generator) can works like a pipe, so you can make a pipeline,
# but the chain must end in a simple generator

# the yield from x expression does with the x object is to call iter(x) to
# obtain an iterator from it. This means that x can be any iterable.

# The main feature of yield from is to open a bidirectional channel
# from the outermost caller to the innermost subgenerator, so that
# values can be sent and yielded back and forth directly from them,
# and exceptions can be thrown all the way in without adding a lot
# of exception handling boilerplate code in the intermediate coroutines.
# This is what enables coroutine delegation in a way that was not possible before.

# The delegating generator resumes when the subgenerator returns and
# the interpreter raises StopIteration with the returned value attached.


def sub_gene():
    total = 0.0
    while True:
        x = yield
        if x is None:
            break
        total += x
    return total


# The value of the yield from expression is the first argument to the StopIteration
# exception raised by the subgenerator when it terminates.
# so you don't have to fetch the value in the error and make the assignment yourself
# NOTE:
# the yield from subgenerator() will assume the subgenerator is not primed and primes
# it automatically, so you only have the prime the delegating generator
def dele_gene(l):
    # without this Loop, when caller called send(None), a StopIteration raised
    # since the code can not reach the next yield from line, it just ended. So
    # it raise a StopIteration just like any generator would do when it ends
    while True:
        v = yield from sub_gene()  # each iteration create a new subgen()
        l.append(v)


def caller():
    l = []
    dg = dele_gene(l)
    next(dg)
    dg.send(1)
    dg.send(2)
    dg.send(3)
    # subgen receive send(None) and finish, raise StopIteration that make delegating gen resume
    # Without the last .send(None) the averager subgenerator never terminates,
    # the delegating generator group is never reactivated, and the assignment
    # to variable v never happens.
    dg.send(None)
    print(l)
    dg.send(4)
    dg.send(5)
    dg.send(6)
    dg.send(None)
    print(l)


caller()
