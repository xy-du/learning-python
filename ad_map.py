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

# accepts either another dictionary object or an iterable of key/value pairs (as tuples or other iterables of length
# two).here if you only pass (('Japan', 111)) in without the comma, what you actually pass in is just ('japan',111)
# iterable, yes, but the element will be 'Japan' and 111, which apparently will not work
# instead, you should pass in like below, then ('Japna',111) in (('Japan', 111),) will be seen as the first element.
country_dict.update((('Japan', 111),))
print(country_dict)

# handle missing key with setdefault
# as we can see, the logic of three line can be expressed by single line with setdefault key
# compile() will return a match object of regular expression
# enumerate(iterable, startindex) will return each item in iterable with index starting from 1, in the form(item,index)
# finditer() will return every single match in the form of match object, group() can get the actual string content
# setdefault(key,val) if find the value of the key, then return. if not, add the key:val pair into map and return it.
# use defaultdict(factory) instead of flat dict. __missing__ in it, only called by __getitem__ (map[key]), not other
# method(map.get(method)), the factory is holding in an instance attribute called default_factory
import re
import collections

pattern = re.compile('\w+')
# record = {}
record = collections.defaultdict(list)
fp = open('zen.txt', encoding='utf-8')
for line_no, line in enumerate(fp, 1):
    for match in pattern.finditer(line):
        word = match.group()
        column_no = match.start() + 1
        location = (line_no, column_no)
        # word_rec = record.get(word, [])
        # word_rec.append(location)
        # record[word] = word_rec
        # record.setdefault(word, []).append(location)
        record[word].append(location)
fp.close()
# comment it since the output is too much
# for w in sorted(record, key=str.upper):
#     print(w, record[w])

# a little case to show that the keys in map do not have to be the same type
m = {'key1': 1, 22: 2}
print(m)


# about __missing__ method
# __missing method is not defined in the base dict class, but dict is aware of it. if you subclass dict and provide
# this method, the standard __getitem__ will call it whenever a key is not founded
# this method will only be used by __getitem__(map[key]), will not be used by __contain__(in operator) and get(key)

# implement a dict that the key type mixing str and int type but when you use it, you can use the way you like and the
# int-to-str operation will performed automatically. i.e. if value not found in int form key it will be convert to
# string and try again

class StrKeyDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):  # not with this test, when str(key) is not in dict, infinite recursion happen
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default):
        try:
            return self[key]  # user self[] so the __missing__ will be invoked when self[key] is not there
        except KeyError:
            return default

    # item in self.keys() to make sure when int key has it's value, the logic is right.
    # after all, we want this class to be 'friendlier' but not limit the key type to just str
    def __contains__(self, item):
        return item in self.keys() or str(item) in self.keys()


d = StrKeyDict([('2', 'two'), ('4', 'four')])

print(d[2])
print(d['2'])
# print(d[3]) # error
# print(d['3']) # error

# variations of dict
# mapping types in the standard library module collections
# defaultdict   see before
# collections.OrderedDict   as you can guess.  popitem()   popitem(last=True)
# collections.ChainMap    holds a list of mappings that can be searched as one
# collections.Counter   count each item happened how many times in a iterable or mapping
# collections.UserDict   pure python implementation of a mapping just like the dict but it's designed to be subclassed
