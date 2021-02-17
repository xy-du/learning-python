# first, Python programmers are not strict about this distinction:
# generators are also called iterators, even in the official docs
# iterator and generator are fairly close synonyms

# but, if you try to see detailed relationship between them, there are some view points you can take:

# iterface viewpoint:
# iterator protocal: __iter__  and  __next
# generator object implements both, so generator is also iterator

from collections import abc

en = enumerate('ABC')
print(isinstance(en, abc.Iterator))
ge = (n for n in [1, 2, 3])
print(isinstance(ge, abc.Iterator))

# implementation viewpoint:
# In python, you get generator object in two way: generator function and generator expression
# the generator object you get from these two way are instance of internal Generator Type,
# they are iterator, since generator implement the iterator interface
# but not every iterator is generator, and you can create one of these just by implementing
# the classic iterator pattern
import types

print(isinstance(en, types.GeneratorType))
print(isinstance(ge, types.GeneratorType))

# conceptual level:
# iterator:
# however much logic is in a classic iterator, it always reads values from
# an existing data source, and when you call next(it), the iterator is not
# expected to change the item it gets from the source, it’s supposed to just yield it as is.
# generator:
# In contrast, a generator may produce values without necessarily traversing a collection,
# like range does. And even if attached to a collection, generators are not
# limited to yielding just the items in it, but may yield some other
# values derived from them
