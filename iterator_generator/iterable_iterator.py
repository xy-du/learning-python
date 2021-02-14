# iterable
#   Any object from which the iter built-in function can obtain
#   an iterator.
#       1. Objects implementing an __iter__ method returning an iterator
#       are iterable.
#       2.Sequencesare always iterable; as are objects implementing a
#   __  getitem__ method that takes 0-based indexes.

# iterator
#   1. Any object that implements the __next__ no-argument method that
#   returns the next item in a series or raises StopIteration when there
#   are no more items.
#   2.  Python iterators also implement the __iter__ method so they are
#   iterable as well. but it often just return self
# NOTE:
# standard iterator interface has two methods:
# __next__
#   Returns the next available item, raising StopIteration when there are no more items.
# __iter__
#   Returns self; this allows iterators to be used where an iterable is expected,
#   for example, in a for loop.
# NOTE:
# the best way to check if an object x is an iterator is to call isinstance(x, abc.Iterator)
# Thanks to Iterator.__subclasshook__, this test works even if the class of x is not a real
# or virtual subclass of Iterator.

# relationship between iterator and iterable
#   python obtain iterator from iterable


s = 'ABC'
for c in s:
    print(c)
# the s here is iterable, you don't see it, but there is an
# iterator work behind the scene

# here is how you emulate the process by hand
s = 'ABC'
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break

# StopIteration signals that the iterator is exhausted.
# This exception is handled internally in for loops and other
# iteration contexts like list comprehensions, tuple unpacking, etc.

from iterator_generator.sentence_v1 import Sentence

st = Sentence('it is good')
it = iter(st)
print(next(it))
print(next(it))
print(next(it))
# one more , it will cause StopIteration error
# print(next(it))
print(list(it))  # the list is empty, so once exhausted, and iterator becomes useless
print(list(iter(st)))  # a new iterator must be created
