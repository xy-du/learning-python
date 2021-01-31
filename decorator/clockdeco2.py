import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - t0
        arg_list = []
        name = func.__name__
        if args:
            arg_list.append(','.join(repr(arg) for arg in args))
        if kwargs:
            arg_list.append(','.join('%s=%r' % (k, v) for k, v in sorted(kwargs.items())))
            print(arg_list)
        args_str = ','.join(arg_list)
        print('[%0.8fs] %s(%s) --> %r' % (elapsed_time, name, args_str, result))
        return result

    return clocked
