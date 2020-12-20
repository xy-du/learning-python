from collections import abc

# collections.abc, this used to test whether a class provides a particular interface; for example, whether it is
# hashable or whether it is a mapping.
# Mapping and MutableMapping ABCs(abstract base class) in this module formalize the interface of dict and similar type
# special mappings usually extend dict ro collections.UserDict instead of these ABCs, these are more often used as
# criteria for isinstance() test
# isinstance() test is better when checking the function arguments type, because alternative mapping types can be used
my_map = {}
print(isinstance(my_map, abc.Mapping))
print(type(my_map))

# key of dict type must be hashable, and all mapping types in std use the basic dict in their implementation
# so they share the same limitation that the keys must be hashable
# so what is hashable?
# an object has hash value that never change during its lifetime(needs __hash()__ method) and can be compared with
# other objects(it has __eq()__ method). hashable objects which compares equal must have the same hash value
# atomic immutable types(str, bytes, numeric types) are all hashable
# its hashability that makes an object can be the dict key since the structure use the hash value internally
# most of python's immutable built-in objects are hashable(only hashable if their elements are hashable),
# mutable objects are not.
# instances of user-defined classes are hashable by default.they all compared unequal and their hash value is
# derived from their id()
t1 = (1, 2, (30, 40))
print(hash(t1))
t2 = (1, 2, [30, 40])
# print(hash(t2)) # this one will cause an error
t3 = (1, 2, frozenset([30, 40]))
print(hash(t3))

# dict can be built in several ways
a = dict(one=1, two=2, three=3)
d = {'one': 1, 'two': 2, 'three': 3}
e = dict({'one': 1, 'two': 2, 'three': 3})
b = dict([('one', 1), ('two', 2), ('three', 3)])
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(a == b == c == d == e)

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]

country_dict = {country: code for code, country in DIAL_CODES}
print(country_dict)
country_dict_filtered = {country: code for code, country in DIAL_CODES if code < 66}
print(country_dict_filtered)
# note that this one is coming from the items()
country_dict_f = {country: code for country, code in country_dict.items() if code < 66}
print(country_dict_filtered)
