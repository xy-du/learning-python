# What is generator function:
# Any Python function that has the yield keyword in its body
# is a generator function: a function which, when called, returns
# a generator object. In other words, a generator function is a generator factory.
def gen_123():
    yield 1
    yield 2
    yield 3


print(gen_123)  # just a function
print(gen_123())  # but it return a generator
for i in gen_123():  # Generators are iterators that produce the values of the expressions passed to yield.
    print(i)

ge = gen_123()
print(next(ge))
print(next(ge))
print(next(ge))


# one more and it will cause a error : StopIteration
# because the body of the function completes
# print(next(ge))

# NOTE: how generator function works
# A generator function builds a generator object that wraps
# the body of the function. When we invoke next(...) on the generator
# object, execution advances to the next yield in the function body,
# and the next(...) call evaluates to the value yielded when the function
# body is suspended. Finally, when the function body returns, the enclosing
# generator object raises StopIteration, in accordance with the Iterator protocol.

def gen_AB():
    print('begin')
    yield 'A'
    print('middle')
    yield 'B'
    print('end')


i = 1
for c in gen_AB():
    print('index:', i)
    print(c)
