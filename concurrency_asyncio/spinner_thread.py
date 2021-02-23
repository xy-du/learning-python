# run this in terminal with the 'Python' command so the spinner trick
# with the output can show

import itertools
import threading
import time


def spin(msg, done):
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        print(status, flush=True, end='\r')
        if done.wait(.1):  # wait for 0.1 sec to see if the internal flag has been set to true
            break
    # print(' ' * len(status), end='\r')


def slow_function():
    # pretend waiting a long time for I/O
    time.sleep(3)
    return 42


def supervisor():
    done = threading.Event()  # a simple mechanism for communication for threads
    spinner = threading.Thread(target=spin,
                               args=('thinking!', done))
    print('spinner object:', spinner)
    spinner.start()
    result = slow_function()
    done.set()  # make the internal flag be true
    spinner.join()
    return result


def main():
    result = supervisor()
    print('Answer:', result)


if __name__ == '__main__':
    main()
