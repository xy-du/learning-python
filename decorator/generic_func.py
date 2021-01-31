# use single dispatch to bundle several functions into a single generic function

import functools
from collections import abc
import html
import numbers


# this generic funtion is to generate different html content based on the data type

# NOTE: python do not support method or function overloading like java and c++ do
# if we use the if/elif/elif way to create this dispatcher, this is not extensible and over time, the function will
# become too large
# The new functools.singledispatch decorator in Python 3.4 allows each module to contribute to the overall solution,
# and lets you easily provide a specialized function even for classes that you can’t edit.
# If you decorate a plain function with @singledispatch, it becomes a generic function: a group of functions to perform
# the same operation in different ways, depending on the type of the first argument
# singledispath function according to the first argument and this is why it's 'single' dispath, if more arguments were
# used to select the specific functions, we'd have multiple-dispatch

# notable quality of single dispatch mechanism is that you can register specialized function anywhere in the system,
# in any module. and you can write custom functions for classes that you did not write and can not change

# A single class with many overloaded variations of a method is better than a single function with a lengthy stretch
# of if/elif/elif/elif blocks. But both solutions are flawed because they concentrate too much responsibility in a
# single code unit—the class or the function. The advantage of @sin gledispath is supporting modular extension:
# each module can register a specialized function for each type it supports.

# NOTE:
#   @base_function.register(type) is how you contribute
#   name of the specialized functions is irrelevant and _ is a good choice to make this clear
#   when possible, register the specialized functions to handle ABCs(abstract classes) such as numbers.Integral and
# abc.MutableSequence instead of concrete implementations like int and list
#   you can stack register decorators to support different types with the same functions
@functools.singledispatch  # create a generic function
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}<pre>'.format(content)


@htmlize.register(numbers.Integral)  # use ABCs (abstract classes) to register whenever possible
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(str)
def _(text):
    return html.escape(text).replace('\n', '<br>\n')


@htmlize.register(tuple)  # stack decorators to make specialized method to handle mutiple type
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<li>\n<li>' + inner + '<li>\n<li>'


print(htmlize({1, 2, 3}))
print(htmlize(23))
print(htmlize('first line & first item \n second line & second item\n'))
print(htmlize(['abcde', 66, {3, 2, 1}]))
