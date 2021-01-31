import weakref

#############################################
# run separately on the python console
# select this fragment and option+shift+E in Pycharm
#############################################
s = {1, 2, 3}
wef = weakref.ref(s)

###########################
# Then run these statement one by one on the console
###########################
# wef()
# s={2,3,4}
# wef() is None
# wef() is None

# after s={2,3,4}, wef() is None did not return True, that is because that there is a special variable _ when
# you run program in the python console, it hold the result of the last output, which it's the output of
# first wef() call, so _ hold the reference to the {1,2,3} until it rebind to the result returned by the first
# wef() is None, which is the False. That when there is no reference to the {1,2,3} and it's be destroyed and
# the next time you call wef() is None it return true

# weak reference is useful when you want hold a reference to a object yet do not want interrupt the garbage
# collection process, since weak reference do not increase the reference count

# weakref.ref class is low-level interface intended for advanced use
# most of the time, we use weakref collections and finalize method:
# WeakKeyDictionary  weakValueDictionary  WeakSet  finalize
