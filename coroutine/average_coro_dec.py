from functools import wraps


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@coroutine
def average():
    cnt = 0
    total = 0.0
    ave = None
    while True:  # only terminate when call .close() on it, or by GC when no reference to it
        x = yield ave
        total += x
        cnt += 1
        ave = total / cnt


if __name__ == '__main__':
    ave = average()
    # thanks to the decorator we created, priming is not needed any more
    # next(ave)  # priming
    print(ave.send(10))
    print(ave.send(20))
    print(ave.send(30))
