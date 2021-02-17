from random import randint


def d6():
    return randint(1, 6)


# this will return a iterator
it = iter(d6, 1)
print(it)
for i in it:  # keep running until it runs into 1
    print(i)
