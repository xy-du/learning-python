# every class has an interface: the set(fixed) public attributes(methods or data attributes) implemented or inherited
# by the class, this include special method like __getitem__ and __len__
#   1. private and protected attributes are not considered as a part of interface
#   2. why even data attributes? because if necessary, we can always turn them into a property implementing
#       getter/setter logic without change any parts of the code of the rest.(see the following example)

# class CA:
#     def __init__(self,x):
#         self.x=x

# change the CA to the following
# and the underlying are changed, but user can still read attribute as my_CA.x
class CA:
    def __init__(self, x):
        self.__x = x

    @property
    def x(self):
        return self.__x

# you do not see the 'interface' in python the way you see it in, say, JAVA, here it's more 'dynamic'

# In python, interface/protocol are basically the same:
# the subset of an object’s public methods that enable it to play a specific role in the system, A class may implement
# several protocols, enabling its instances to fulfill several roles.
# protocol are interface, and it's informal interface, defined only by documentation and convention, it can
# not be forced like normal interface. And you can implement just a part of it. eg., Sometimes all a specific API
# requires from “a file-like object” is that it has a .read() method that returns bytes. The remaining file methods
# may or may not be relevant in the context.

# X-like object,” “X protocol,” and “X interface” are synonyms in the minds of Pythonistas.
