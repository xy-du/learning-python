print('abc'.__class__)
print(str.__class__)
from cls_metaprogram.bulkfood_v6 import LineItem

print(LineItem.__class__)
print(type.__class__)
# every python class is the instance of type, directly or indirectly;
# to avoid infinite regress, type is an instance of itself

import collections.abc
import abc

print(collections.abc.Iterable.__class__)  # abc.ABCMeta
print(abc.ABCMeta.__class__)  # whose superclass is type
# every python class is the instance of type, directly or indirectly;
# but only the metaclass is also the subclass of type,such as ABCMeta, so
# they inherit the power toe construct class from type. a metaclass can
# customize its instances by implementing __init__. A metaclass __init__
# method can do everything a class decorator can do.
