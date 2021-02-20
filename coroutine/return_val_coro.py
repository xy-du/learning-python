# in order to return a value, a coroutine has to end normally

# when ended normal, the generator object raises StopIteration.
# The value attribute of the exception carries the value returned.

# the value of the return expression is smuggled to the caller as
# an attribute of the StopIteration exception.

def coro_ave():
    cnt = 0
    total = 0.0
    while True:
        x = yield
        if x is None:
            break
        total += x
        cnt += 1
    return total / cnt


ca = coro_ave()
next(ca)
ca.send(10)
ca.send(20)
try:
    ca.send(None)
except StopIteration as st:
    print(st.value)
