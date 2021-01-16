import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)  # the func here is actually a free variable, closure for clocked encompassed it
        elapsed_time = time.perf_counter() - t0
        name = func.__name__
        args_str = ','.join(repr(a) for a in args)
        print('[%0.8fs] %s(%s) --> %r' % (elapsed_time, name, args_str, result))
        return result

    return clocked
