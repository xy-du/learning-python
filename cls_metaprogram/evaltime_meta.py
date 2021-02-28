# run in two ways:
# console: import evaltime
# terminal: python evaltime.py
# to understand the behave of metaclass
# specially, please pay attention to the affect that
# metaclass take on the subclass whose superclass take
# a metaclass as one of its arguments, you will find that the
# affects get inherited

from evalsupport import MetaAleph
from evalsupport import deco_alpha

print('<[1]> evaltime_meta module start')


@deco_alpha
class ClassThree():
    print('<[2]> ClassThree body')

    def method_y(self):
        print('<[3]> ClassThree.method_y')


class ClassFour(ClassThree):
    print('<[4]> ClassFour body')

    def method_y(self):
        print('<[5]> ClassFour.method_y')


# NOTE:
# The Python interpreter evaluates the body of ClassFive
# but then, instead of calling type to build the actual class body,
# it calls MetaAleph. Looking at the definition of MetaAleph
# you’ll see that the __init__ method gets four arguments:
# self:
# the class object being initialized
# name,bases,dic
# the same arguments passed to type to build a class

class ClassFive(metaclass=MetaAleph):
    print('<[6]> ClassFive body')

    def __init__(self):
        print('<[7]> ClassFive.__init__')

    def method_z(self):
        print('<[8]> ClassFive.method_y')


# Note that ClassSix makes no direct reference to MetaAleph,
# but it is affected by it because it’s a subclass of ClassFive
# and therefore it is also an instance of MetaAleph,
# so it’s initialized by MetaAleph.__init__.
class ClassSix(ClassFive):
    print('<[9]> ClassSix body')

    def method_z(self):
        print('<[10]> ClassSix.method_y')


if __name__ == '__main__':
    print('<[11]> ClassThree tests', 30 * '.')
    three = ClassThree()
    three.method_y()
    print('<[12]> ClassFour tests', 30 * '.')
    four = ClassFour()
    four.method_y()
    print('<[13]> ClassFive tests', 30 * '.')
    five = ClassFive()
    five.method_z()
    print('<[14]> ClassSix tests', 30 * '.')
    six = ClassSix()
    six.method_z()

print('<[15]> evaltime_meta module end')
