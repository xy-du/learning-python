# descriptor
# A class implementing a __get__, a __set__, or a __delete__ method
# is a descriptor. You use a descriptor by declaring instances
# of it as class attributes of another class.

#  The property class implements the full descriptor protocol.
#  As usual with protocols, partial implementations are OK. In fact,
#  most descriptors we see in real code implement only __get__ and __set__,
#  and many implement only one of these methods.

# Descriptor Class:
# A class implementing the descriptor protocol

# Managed Class:
# The class where the descriptor instances are declared as class attributes

# Descriptor Instance:
# Each instance of a descriptor class, declared as a class attribute of the managed class

# Managed Instance
# the instance of the managed Class

# Storage attribute
# An attribute of the managed instance that will hold the value of a managed
# attribute for that particular instance

# Managed attribute
# A public attribute in the managed class that will be handled
# by a descriptor instance, with values stored in storage attributes.
# In other words, a descriptor instance and a storage attribute provide
# the infrastructure for a managed attribute.

class Quatity:
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('value must be > 0')
    # NOTE:
    # self and instance. Here, self is the descriptor instance,
    # which is actually a class attribute of the managed class.
    # You may have thousands of LineItem instances in memory at one time,
    # but you’ll only have two instances of the descriptors:
    # LineItem.weight and LineItem.price.
    # So anything you store in the descriptor instances themselves
    # is actually part of a LineItem class attribute,
    # and therefore is shared among all LineItem instances.
    # that is why here we do not use the :
    # self.__dict__[name]=value


class ItemLine:
    weight = Quatity('weight')
    price = Quatity('price')

    def __init__(self, description, weight, price):
        self.decription = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    it = ItemLine('banana', 10, -10)  # works as expected, here will be error
    print(it.subtotal())
