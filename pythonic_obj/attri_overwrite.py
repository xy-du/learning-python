# class attribute can be used as default values for instance attribute， see self.typecode in class Vector.

# If you write to a instance attribute that does not exist, you create a new instance attribute, and the class
# attribute with the same name is untouched, but it will be overwrite by the instance attribute when call self.var

from vector import Vector

v1 = Vector(1, 2)
dump = bytes(v1)
print(dump)
print(len(dump))
# make a new instance attribute with the same name as class attribute
v1.typecode = 'f'
# in __bytes__, self.typecode is used, as we can see, it's the instance attribute instead of class attribute now
dump = bytes(v1)
print(dump)
print(len(dump))

# if you want to change the class attribute you have to set it on the class directly
# we can also see that the change we made here has no effect on the instance
Vector.typecode = 'd'
dump = bytes(v1)
print(dump)
print(len(dump))
# but this is not the idiomatic way, which is change it through subclass
