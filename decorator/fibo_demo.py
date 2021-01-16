from clockdeco2 import clock


# here is a silly recursive algorithm, and with clock decorator, you can see the same function with the same argument
# get called again and again, which will be nightmare if the computation is very expensive (which is not the case here)
# see fibo_demo_lru.py in this directory
@clock
def fibonacci(n):
    return 1 if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(6))
