# run this in terminal so you can see the spinning cursor
import asyncio
import itertools


async def spin(msg):  # <1>
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        print(status, flush=True, end='\r')
        try:
            await asyncio.sleep(.1)  # <2>
        except asyncio.CancelledError:  # <3>
            break
    print(' ' * len(status), end='\r')


async def slow_function():  # <4>
    # pretend waiting a long time for I/O
    await asyncio.sleep(3)  # do not call the time.sleep that will block main thread that loop running in
    return 42


async def supervisor():  # <6>
    spinner = asyncio.create_task(spin('thinking!'))  # schedule the coro
    print('spinner object:', spinner)
    result = await slow_function()
    spinner.cancel()  # <10>
    return result


def main():
    result = asyncio.run(supervisor())  # entry point for asyncio program
    print('Answer:', result)


if __name__ == '__main__':
    main()
