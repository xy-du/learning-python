# first-class function :  functions as first-class objects
# first-class:
# create at runtime
# can be assigned to a variable or element in data structure
# can be passed to a function
# can be returned from a function

def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


# print(factorial(42))
# print(factorial.__doc__)
# print(type(factorial))
#
fact = factorial
# print(fact)
# fact(5)
# print(map(factorial, range(11)))
# print(list(map(fact, range(11))))


# high-order functions:
# receive function as args, return function as result
# eg.  map, filter, reduce, apply
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']


# print(sorted(fruits, key=len))


def reverse(words):
    return words[::-1]


# the origin data is not changed
# print(sorted(fruits, key=reverse))

l1 = list(map(fact, range(6)))
l2 = [fact(n) for n in range(6)]
l3 = list(map(fact, filter(lambda n: n % 2, range(6))))
l4 = [fact(n) for n in range(6) if n % 2]
# print(l1)
# print(l2)
# print(l3)
# print(l4)

from functools import reduce
from operator import add

# print(reduce(add, range(100)))
# print(sum(range(100)))

# lambda is used to create an anonymous function
# pure expression.  can not make assignment or use any other Python statement such as while,try,etc
# the best use of anonymous functions is in the context of an argument list.
# outsize the arguments to higher-order functions, anonymous functions are rarely useful in Python
# print(sorted(fruits, key=lambda word: word[::-1]))

# seven callable objects in python
# built-in function.  len  time.shrftime
# built-in method   dict.get
# user-defined functions
# method.   functions defined in the body of a class
# class.   __new__   __init__   then return new object to caller
# class instances.   if a class implements __call__  method. its instance can be invoked as a function
# generator function.    method or function using the yield keywords to return a generator

# the safiest way to determine if an object is callable is use the callable() built-in:
# print([callable(obj) for obj in (abs, str, 123)])


# not only Python function can be object, object can be made to behave like function.
# implement a __call__ instance method is all it takes
import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self, *args, **kwargs):
        return self.pick()


bingo = BingoCage(range(3))


# print(bingo.pick())
# print(bingo())
# print(callable(bingo))


# function object has many attributes beyond __doc__, see below
# print(dir(factorial))


# like the instances of user-defined class, function use __dict__ to store its attributes
# assign arbitrary attribute to functions is not a common prctice in general, but it can be done, and Django use
# this a lot
# we put our attentio to the attributes that is specific to functions and not in the general classes
# eg. __code__ __defaults__  __annotations__ in this 'special set' will be used by IDEs and framework
class C:
    pass


def func():
    pass


obj = C()


# print(set(dir(func)) - set(dir(obj)))

# Positional arguments: just normal type we see a lot, a simple name there, and python will give it its value based on
#                       there p=position, order matters in this type of arguments
# default value argument: arg_name=default_value, by this way, when the arg_name is not give a specific value,
#                         default_value will be used
# keyword arguments: this is more on the calling side, when call a function, use explicit arg name to pass the value
#                    in the key=value form
# arbitrary number of arguments:
#       arbitrary arguments: *args, receive arbitrary number of values, used for 'iterables'
#       arbitrary keyword arguments: **args, receive arbitrary number of key-value pairs, used for 'mappings'
# keyword-only arguments:
#       function(a,*b,c), here the c argument if the keyword-only arguments, because if you do not use keyword format
#       to pass the value, *b will 'intercept' all the values except the one for a, eg. function(1,2,3,c=4)

# THE POST IMPORTANT RULEs!!!
# python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter

def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


# print(tag('name', 'A_Content'))
# print(tag('name', 'A_Content', 'B_Content'))
# print(tag('name', 'A_Content', cls='B_Content'))  # keyword-only argument cls
# print(tag('name', key1='value1', key2='value2'))
# print(tag('name', key1='value1', key2='value2', cls='classvalue'))  # **args will not affect keyword argument
# params = {'name': 'name', 'cls': 'classvalue', 'key1': 'value1', 'key2': 'value2'}
# print(tag(**params))  # **params passes all its items as separate arguments
# # **args makes me think of the *tuple way to pass the example
# tp = ('name', 'A_Content', 'B_Content')
# print(tag(*tp))  # apparently, this can not manage the key:value style argument value passing

# def clip(text, max_len=80):
#     end = None
#     if len(text) > max_len:
#         space_index = text.rfind(' ', 0, max_len)
#         if space_index >= 0:
#             end = space_index
#         else:
#             space_index = text.find(' ', max_len)
#             if space_index >= 0:
#                 end = space_index
#     if not end:
#         end = len(text)
#     return text[:end]


# __default__ holds the value of the default value of the positional and keyword arguments in a tuple, but these values
# is identified only by its position, so to link them respectively with their arguments which you get by combining
# __code__.co_varcount and __code__covarnames described below, you have to scan it from the last to the first
# By the way, the defaults value of keyword-only arguments appear in __kwdefaults__
# note here are only the default values, the args name are in the __code__ object
# print(clip.__defaults__)
# __code__  is a reference to a code object, which hold the name of the arguments
# print(clip.__code__)
# arguments is the fist N=__code__.co_argcount strings, since it also include the names of the local variables
# and co_varnames include the names of *arg and **arg type of arguments (appearing after the positional and keyword
# arguments name), while co_argcount does not count these types
# print(clip.__code__.co_varnames)
# print(clip.__code__.co_argcount)

# as we can see, the way above to gain inspection is very inconvenient
# luckily, there is a module called inspect
from inspect import signature

sig = signature(tag)
# print(sig)
# for name, params in sig.parameters.items():  # sig.parameters is a ordered mapping
#     print(name, params.name, params.default, params.kind)  # there 5 kinds of _ParameterKind

# Signature has a method : bind.
# take any number of arguments and binds them to the parameters in the signature, applying the usual rules for
# matching actual arguments to formal parameters
# this can be used by a framework or IDE to validate arguments prior to the actual function invocation.

my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
bound_args = sig.bind(**my_tag)


# for name, value in bound_args.arguments.items():
#     print(name, value)

# remove the name attribute in the arguments will break the arguments-parameters-binding rule python using and
# cause an TypeError: missing a required argument:'name'
# frameworks and toools like IDE can use the information to validate code
# del my_tag['name']
# bound_args = sig.bind(**my_tag) #TypeError: missing a required argument: 'name'


# function annotations
# annotated version of clip
# annotation expression preceded by :
# you can see how to annotate arguments and return value in the first line
# NO processing is done by annotation, it's merely stored in the __annotations__ attribute of the function
# annotation has NO meaning of python interpreter
# maybe it can be used by framework and IDE to do some checking or setting
def clip(text: str, max_len: 'int > 0' = 80) -> str:
    end = None
    if len(text) > max_len:
        space_index = text.rfind(' ', 0, max_len)
        if space_index >= 0:
            end = space_index
        else:
            space_index = text.find(' ', max_len)
            if space_index >= 0:
                end = space_index
    if not end:
        end = len(text)
    return text[:end]


# print(clip.__annotations__)

# inspect.signature() knows how to extract the annotations
sig = signature(clip)
# print(sig.return_annotation)
for param in sig.parameters.values():
    format_name = repr(param.name).ljust(10)
    # print(format_name, param.annotation)

# packages for functional programming

# the operator module
# so what in it to use operator module?
# consider you want to multiply a sequence of numbers to calculate factorials without using recursion
# you can use reduce and lambda, but it's trivial, since you hve to multiply two items of the sequence
from functools import reduce


def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))


# print(fact(5))

# but if you use the mul function from operator module, well, see for yourself:
from operator import mul


def fact_op(n):
    return reduce(mul, range(1, n + 1))


# print(fact_op(5))

# Another group of one-trick lambdas that operator replaces are functions to pick items from sequences or read
# attributes from objects: itemgetter and attrgetter actually build custom functions to do that.

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

# get the field of a collection you link together or pass in.
from operator import itemgetter

# for city in sorted(metro_data, key=itemgetter(1)):
#     print(city)

cc_name = itemgetter(1, 0)
# for city in metro_data:
#     print(cc_name(city))

# a sibling of itemgetter is attrgetter, which creates functions to extract object at attributes by name

from collections import namedtuple
from operator import attrgetter

# it's the best to name the variable exact the same of the first argument 'typename' ?? en... I think so..
LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')

metro_date_ls = [Metropolis(name, cc, pop, LatLong(lat, long))
                 for name, cc, pop, (lat, long) in metro_data]

# print(metro_date_ls[0])
# print(metro_date_ls[0].coord.lat)

# here, again, we can see that the tuple can not only be seen as a immutable sequence, but a set of record
# with every field in it named and a light weight solution for class.
name_lat = attrgetter('name', 'coord.lat')
# for city in sorted(metro_date_ls, key=attrgetter('coord.lat')):
#     print(name_lat(city))

# methodcaller, just like itergetter and attrgetter, it create a method on the fly, the function it create calls
# the method of the object given as a argument.

from operator import methodcaller

s = 'The time has come'
upper_caller = methodcaller('upper')
# print(upper_caller(s))

# freezing arguments
hiphenate = methodcaller('replace', ' ', '-')
print(hiphenate(s))

# functools module brings a lot higher-order functions
# the best known of them is reduce
# of the remaining functions in functools, the most useful is partial and its variation, partialmethod
# partial produce a callable with some of the arguments of the original function fixed, this is useful to adapt a
# function that takes one or more arguments to an API that requires a callback with fewer argumemts
# partialmethod is new in python3.4, it does the same job as partial, but is designed to work with methods.

from operator import mul
from functools import partial

triple = partial(mul, 3)
print(triple(7))
print(list(map(triple, range(1, 10))))

from unicodedata import normalize

s1 = 'codé'
s2 = 'code\u0301'
nfc = partial(normalize, 'NFC')
print(s1, s2)
print(s1 == s2)
print(nfc(s1), nfc(s2))
print(nfc(s1) == nfc(s2))

# partial takes a callable as first argument, followed by an arbitrary number of positional and
# keyword arguments to bind

img_tag = partial(tag, 'img', cls='pic-frame')
print(img_tag)
print(img_tag(src='dxy.jpg'))
print(img_tag.func)
print(img_tag.args)
print(img_tag.keywords)
