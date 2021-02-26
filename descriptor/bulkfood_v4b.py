class Quantity:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        cls_name = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(cls_name, index)
        cls.__counter += 1

    # support introspection and other metaprogramming tricks by the user,
    # it’s a good practice to make __get__ return the descriptor instance
    # when the managed attribute is accessed through the class
    def __get__(self, instance, owner):
        if instance is None:  # access thought class directly will cause this
            return self
        else:
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
    print(ItemLine.price)
