dxy = {'name': 'dxy', 'age': 25}
austin = dxy
print(austin == dxy)
print(id(austin), id(dxy))
print(dxy is austin)

little_d = {'name': 'dxy', 'age': 25}
print(little_d is dxy)  # False, they are two different object
print(id(little_d), id(dxy))  # id is different
print(little_d == dxy)  # base on their content, they are equal

# think of id as its memory address, aliases should have the same id, and the is operator applied on them should
# return True (because of the same id)
# == compares the value of the object, in another word, it compares the content

# most of the time, we care more about the content of the variables instead of the identities, so we may
# see == more. But when you compare variable with singleton, it make sense to use is operator.
# the most common case is checking weather a variable is bound to None
# is operator is faster than == operator since it can not be overloaded, it simply compare the ids.
# In contrast, == operator will use __eq__() mathod.
# Truth is, __eq__() inherited from object compares IDs, but most built-in types override __eq__ with more
# meaningful implementations that actually take into account the value of the object attributes.
a = None
print(a == None)
