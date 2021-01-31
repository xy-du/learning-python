import weakref


# WeakValueDictionary : mutable mapping, values are weak references to objects, when a referred object is
# garbage collected, the corresponding key is automatically removed

# if you need to build a class that is aware of all its instances, a good solution is to create a class
# attribute with a WeakSet to hold the references to the instances. WeakSet hold weak reference of objects

class Cheese():
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese

print(sorted(stock.keys()))
del catalog
print(sorted(stock.keys()))  # amazingly, you can still see cheese Parmesan is still around
del cheese  # and here is the reason, the cheese used in the loop above is a global variable which hold a reference
print(sorted(stock.keys()))  # after the reference that cheese hold get deleted, all the keys in the ref mapping is gone
