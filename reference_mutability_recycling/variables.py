# variables are not box
a = [1, 2, 3]
b = a
a.append(4)
print(b)


# if you put things into two boxs, the changes happeded in one would not affect the other. But this is not the truth
# in this case. So think it as a label may be more accurate.

# we always say, 'assign the object to the variable', but if you think about it, in the label way, the better way to
# put it should be 'ssign the variables to the objects'
# another example to justfy this is that the object is create before the variable, see below
#############################################
# run separately on the python console to see the output and error
# select this fragment and option+shift+E in Pycharm
#############################################
class Gizmo:
    def __init__(self):
        print('Gizimo id : %d' % id(self))


x = Gizmo()
# by this time, you can see x in the.(If an object is not passed to dir() method, it returns the list of names in the
# current local scope.)
dir()
y = Gizmo() * 10  # here, you when evaluate Gizmo() * 10, a error will be raised, and the y will never be create
dir()
