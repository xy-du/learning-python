import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):
    def decorator(func):
        def clocked(*_args):
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ','.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result

        return clocked

    return decorator


@clock()
def snooze1(sec):
    time.sleep(sec)


snooze1(.111)


@clock('{name} -> {elapsed}')
def snooze2(sec):
    time.sleep(sec)


snooze2(.222)
