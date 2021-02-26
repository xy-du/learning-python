# a new Quantity class to avoid repeatedly type the attribute name in the descriptor

# Usually we do not define a descriptor in the same module where
# it’s used, but in a separate utility module designed to be used
# across the application—even in many applications, if you are
# developing a framework.
# so Quantity here is not overworked as it seems like.
class Quantity:
    __counter = 0

    # the storage_name will be like  _Quantity#0
    # the hash sign in it to it will not clash with attributes created by
    # users since the # in it will make it invalid
    def __init__(self):
        cls = self.__class__
        cls_name = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(cls_name, index)
        cls.__counter += 1

    # since the managed attribute will has different name with
    # storage attribute, we can use getattr() without worrying
    # about causing an infinite recur
    # the owner here refer to the managed Class (ItemLine), it's
    # handy when the descriptor is used to get attribute from the class.
    # accessing the attribute through class will make the instance be None
    # for a a better solution see bulkfood_v4b.py
    def __get__(self, instance, owner):
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError('value must be > 0')


class ItemLine:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    print(ItemLine.price)  # AttributeError: 'NoneType' object has no attribute '_Quatity#1'

    it = ItemLine('banana', 10, -10)  # works as expected, here will be error
    print(it.subtotal())
