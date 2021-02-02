# use __format__ can control the formatted displays
#   it's used in built-in format() and str.format()
#   Format Specification Mini-language is extensible so object can have their own presentation code
#   if there is no __format__, when format() is called, __str__ will be used, and if you pass the format
# specifier, a TypeError will rise

brl = 1 / 3
print(brl)
print('{:.2f} hahahha'.format(brl))
print(format(brl, '.2f'))

# self-defined format specification mini-language
# For instance, the classes in the datetime module use the same format codes in the strftime() functions and in
# their __for mat__ methods.
from datetime import datetime

now = datetime.now()
print(format(now, '%H:%M:%S'))
print("it's now {:%I:%M %p}".format(now))

# when you don't have __format__ in you class
from vector_2d import Vector

v = Vector(1.0, 2.0)
print(format(v))
# print(format(v, '.3f')) # this will raise an error
