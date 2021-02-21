from concurrent import futures
from time import sleep, strftime


def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


def loiter(n):
    msg = '{}loiter({}) doing nothing for {}s'
    print(msg.format(n * '\t', n, n))
    sleep(n)
    msg = '{}loiter({}) done'
    print(msg.format(n * '\t', n))
    return n * 10


# when you try to get the result form concurrent.features.Feature with
# result(), if the result is not yet ready, it will get blocked.
# so:
# the for loop in this method will implicitly invoke next(results)
# which in turn will invoke _f.result() on the (internal) _f future
# representing the first call, loiter(0). The result method will block
# until the future is done, therefore each iteration in this loop will
# have to wait for the next result to be ready
def main():
    display('starting......')
    executor = futures.ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, range(5))
    display(results)
    display('waiting for individual results:')
    for i, res in enumerate(results):
        display('result {}:{}'.format(i, res))


if __name__ == '__main__':
    main()

# using the .map() method can ensure you get the result in the
# order that they were first created. this may or may not be helpful
# depending on what you are doing
