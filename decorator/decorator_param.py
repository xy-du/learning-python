# parameterized decorator
# it is not a decorator, strictly speaking, just a decorator factory, when called, it returns the actual decorator
# that will applied to the target function

registry = set()


def register(active=True):
    def decorator(func):
        print('running register<active=%s> -> decorator(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            # registry.remove(func)  do not use reomve, since it will require that func must be a member
            registry.discard(func)
        return func

    return decorator


@register(active=False)
def f1():
    print('this is f1')


print('f1 has just been difined')


@register()
def f2():
    print('this is f2')


print('f2 has just been difined')


def f3():
    print('this is f3')


print('f3 has just been difined')

print(registry)
# you will see that there is only f2 in the set

# note:
# the inner class this the actual decorator
# even you don't want to pass in parameter, the register(decorator factory has to be called as a function), register()
# MAIN Point: the register() return decorator, which is then applied to the decorated function
# register can be used as a regular function, just like decorators

print(register)
register()(f3)
print(registry)
register(active=False)(f3)
print(registry)

# in this example, we did not change the behavior of the function，in order to do that(what a typical decorator will
# do), we need another lavel of nesting.
