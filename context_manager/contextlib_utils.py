# you don't have to always roll you own context manager class
# contextlib in standard library has many useful tools

# here we take a closer look on the @contextmanager decorator

# In a generator decorated with @contextmanager, yield is used to split
# the body of the function in two parts:
# everything before the yield will be executed at the beginning of the
# while block when the interpreter calls __enter__;
# the code after yield will run when __exit__ is called at the end of the block.

import contextlib


# this decorator brings together three distinctive python feature:
# function decorator, generator, with statement
@contextlib.contextmanager
def looking_glass():
    import sys
    origin_writer = sys.stdout.write

    def reverse(text):
        origin_writer(text[::-1])

    sys.stdout.write = reverse
    msg = ''
    try:
        # if there were exception, it will be raise in this yield line
        yield 'ABCDEFG'  # NOTE: the function will pause at this point, value will be bound to target value
    except ZeroDivisionError:
        msg = 'please do not divide by zero!'
    finally:  # you don't know what user will do in the with block, this finally is unavoidable price
        sys.stdout.write = origin_writer
        if msg:
            print(msg)


# Recall that the __exit__ method tells the interpreter that it has
# handled the exception by returning True; in that case, the interpreter
# suppresses the exception. On the other hand, if __exit__ does not
# explicitly return a value, the interpreter gets the usual None,
# and propagates the exception. With @contextmanager, the default behavior
# is inverted: the __exit__ method provided by the decorator assumes any exception
# sent into the generator is handled and should be suppressed.5 You must explicitly re-raise an
# exception in the decorated function if you don’t want @contextmanager to suppress it.


if __name__ == '__main__':
    print('before')
    with looking_glass() as what:
        print('middle')
        print(what)
    print('after')
