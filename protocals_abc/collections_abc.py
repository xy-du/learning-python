# since Python2.6 ABCs are available in the standard library
# most of them are defined in collections.abc
# there are alse some of them in  package io, numbers, for example

# collections.abc
# https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes
# you can see a table in the link, list all the ABCs and their relation, abstract methods,
# concrete methods(mixin method)

#   ABCs        support     with
#   Iterable    iteration   __iter__
#   Container   in          __contains__
#   Sized       len()       __len__

#   main immutable collections        mutable subclasses
#   Sequence                            MutableSequence
#   Mapping                             MutableMapping
#   Set                                 MutableSet

#  from pythons, the object returned from mapping object mthods
#   .item()     .keys()     .values()  | inherited from
#   ItemView    KeysView    ValueView
# the first two inherited from the rich interface Set

# Callable and Hashable
# they are not closely related to collections, but collections.abc was the first package
# defined ABCs in standard library and these two are importance enough to to included
# they are rarely used for inherited, but for isinstance to test if an object is hashable or callable
# NOTE:
# for Callable there is a a callable built-in method, but there is no such one for Hashable
# so isinstance(x, Hashable) is the way to go

# iterable
