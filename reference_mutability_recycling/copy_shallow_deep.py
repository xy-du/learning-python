# copies are shallow by default

# for most built-in mutable collections, a easy way to make a copy is using the constructor
# but not for immutable sequence like tuple
l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)  # copy the data 3, but just the references of list[66, 55, 44] and tuple(7, 8, 9)
l1.append(100)  # the 100 will only exist in l1
l1[1].remove(55)  # 55 will be removed from both l1 and l2 since they refer to the same list
print('l1:', l1)  # l1: [3, [66, 44], (7, 8, 9), 100]
print('l2:', l2)  # l2: [3, [66, 44], (7, 8, 9)]
l2[1] += [33, 22]  # the list changes for both l1 and l2
l2[2] += (10, 11)  # a new tuple was created for l2 and it contains the new data since tuple is immutable
print('l1:', l1)  # l1: [3, [66, 44, 33, 22], (7, 8, 9), 100]
print('l2:', l2)  # l2: [3, [66, 44, 33, 22], (7, 8, 9, 10, 11)]

# for list and other mutable sequence, the shortcut a=b[:] can also make a copy
# but not for immutable sequence like tuple
ls = [1, 2, 3]
ls1 = ls[:]
# ls1 = list(ls)
print(ls1 == ls)  # True, same content
print(ls1 is ls)  # False, copy is performed

tp = (1, 2, 3)
tp1 = tp[:]
# tp1 = tuple(tp)
print(tp == tp1)  # True, same content
print(tp is tp1)  # True, just create a reference, or attach a new label to the data

a = [10, 20]
b = [a, 30]
a.append(b)
print(b)


# deep and shallow copy of arbitrary objects

# the copy module provide the deepcopy and copy method that can perform deep copy or shallow copy
# of Arbitrary Object
class Bus:
    def __init__(self, passenger=None):
        if passenger is None:
            self.bus = []
        else:
            self.bus = list(passenger)

    def drop(self, name):
        self.bus.remove(name)

    def pick(self, name):
        self.bus.append(name)

    def __str__(self):
        return str(self.bus)


# as we can see in the __init__ in the class, list constructor is used to make a new copy of the original data.
# this is something we need to consider about:
# whether the caller expects the arguments passed to be changed. Normally, we follow a best practice of
# interface design 'principle of least astonishment'.
# as a bonus, this solution is more flexible, now the argument passed to the passengers parameter may be a tuple
# or any other iterable, like a set or even database results. because the list constructor accepts any iterable.


import copy

bus = Bus(['aaa', 'bbb', 'ccc', 'ddd'])
bus1 = copy.copy(bus)
bus2 = copy.deepcopy(bus)
bus.drop('aaa')
print(bus1)
print(bus2)

# sometimes, deep copy may not be what we want, that is when you should implement the __cooy__()
# and __deepcopy()__ which is indicated in the copy module document

# NOTE:
# one case when perform a deep copy should be considered: Cyclic Reference
# this will make naive copy algorithm enter into infinite loops
# BUT, don't worry, the deepcopy in copy module handle this situation very well

a = [1, 2, 3]
b = [a, 4, 5]
print(b)
a.append(b)
print(a)  # cyclic reference
c = copy.deepcopy(a)
print(c)  # no error, the deep copy act normally despite the cyclic reference
