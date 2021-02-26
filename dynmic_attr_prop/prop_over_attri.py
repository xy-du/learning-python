# an expression like obj.attr does not search for attr starting
# with obj. The search actually starts at obj.__class__, and
# only if there is no property named attr in the class,
# Python looks in the obj instance itself

class Class:  #
    data = 'the class data attr'

    @property
    def prop(self):
        return 'the prop value'


print('---instance attribute over class attribute-----')
obj = Class()
print(Class.data)
print(obj.data)
print(vars(obj))
obj.data = 'data of obj'
print(vars(obj))  # instance now has its own data attribute
print(obj.data)  # retrieve data from instance will shadow the Class attribute
print(Class.data)  # but retrieve from the class directly is unaffected

print('---class attribute over instance attribute -----')
print(Class.prop)
print(obj.prop)
print(vars(obj))
# obj.prop='property of instance' # this will cause error: AttributeError: can't set attribute
obj.__dict__['prop'] = 'property of instance'  # this is a bypass
print(vars(obj))  # you can see the new prop attribute in it
print(Class.prop)  # unchanged
print(obj.prop)  # still show the property of the class instead of the one of itself
Class.prop = 'balabala'  # this will destroy the property object
# del Class.prop # it  can also be destroyed by this
print(Class.prop)  # now it show the new value
print(obj.prop)  # this is not shadowed by the property anymore since it's been destroyed
