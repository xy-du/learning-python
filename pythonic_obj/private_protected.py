# In python, there is no way to create a private variables like in Java, just a simple mechanism to prevent
# accidental overwriting of 'private' attribute in a subclass

# name mangling:
#   if you name an instance attribute in the form __var (two leading underscores and zero or at most one tailing
# underscore), python will store the name in the instance __dict__ prefixed with a leading underscore and the
# class name. eg. __var will be stored as _CLS__var
#   this is about safety, not security
#   some people think __var is a bad idea, and accidental attribute clobbering should be addressed by naming
# convention. say, you name the attribute directly _MyClass_blahblah

# protected:
#   _var  (single leading underscore), here the var is called 'protected', the single underscore means nothing
# to the python interpreter, but it's a strong convention among Python programmers that you should not access
# such attributes from outside this class.

class Demo:
    def __init__(self, x):
        self.__x = x

    def __str__(self):
        return str(self.__x)


class SubDemo(Demo):
    pass


class SubDemo2(Demo):
    def __init__(self, x):
        self.__x = x

    def __str__(self):
        return str(self.__x)


d1 = Demo(1)
print(d1.__dict__)  # you will see _Demo__x in it
d1.__x = 2  # this has no effect, the __x will still be value 1 not 2
print(d1)
d1._Demo__x = 2  # if you know the name mangling rule, you can change it directly, but you may not want to do this
print(d1)

sd = SubDemo(3)
print(sd.__dict__)  # you still see _Demo__x in it, not _SubDemo__x

sd2 = SubDemo2(4)
print(sd2.__dict__)  # now it's _SubDemo2__x, since you have a new __x (private) in subclass
