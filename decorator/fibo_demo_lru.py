from clockdeco2 import clock
import functools


# NOTE: it's memoIzation, NOT memoRIzation below
# functools.lru_cache() implements memoization: a an optimization technology that works by saving the result of
# previous invocations of an expensive function, avoiding repeat computations on previous computed arguments
# NOTE: lru_cache use the positional and keyword arguments used in the calls, all the arguments taken by the decorated
# function must be hashable
@functools.lru_cache()  # NOTE the parentheses here, reason is that it accepts configuration parameters
@clock  # this is a example of stacked decorators, @lru_cache() is applied on the function returned by @clock
def fibonacci(n):
    return 1 if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(6))

# functools.lru_cache(maxsize=128,typed=true)
#   maxsize: the number of results of calls
#   typed: store results of different argument types separately, i.e., 1 and 1.0 will be stored as two items
