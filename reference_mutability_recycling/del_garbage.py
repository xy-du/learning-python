# del does not delete the object directly, it just delete names

# when the object will be delete
#   CPython: reference counting
#   CPython2.0: add a generational garbage collection algorithm, which can detect groups of objects involved in
#         reference cycle, which maybe unreachable even with outstanding references to them
#   other implementation of Python have more sophisticated garbage collections that do not rely on the reference
#         counting, which means that __del()__ method may not be called immediately when there are no more references
#         to the object

# use weakref.finalize() to register a callback function to be called when an object is destroyed
#############################################
# run separately on the python console
# select this fragment and option+shift+E in Pycharm
#############################################
def bye():
    print('It is time to say goodbye...')


import weakref

s1 = {1, 2, 3}
s2 = s1
ender = weakref.finalize(s1, bye)
###########################
# Then run these statement one by one on the console
###########################
# ender.alive
# del s1
# ender.alive
# s2 = 'spam'
# ender.alive
###########################

# after running the s2 = 'spam', the callback is invoked since this rebinding makes that there is  no reference to
# the {1,2,3} anymore you may wonder: oh! but what about the s1 you pass into finalize(), relax, weak reference is
# used internally and it will not affect the normal garbage collection.
