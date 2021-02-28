import cls_metaprogram.model as model


# we want append the attribute name behind the storage name,
# so it is better for debug, eg:
# storage name is : _NonBlank#0
# we want change it to :_NonBlank#description
# but when the descriptor is instantiated it has no way of
# knowing the name of the managed attribute.
# But once the whole class is assembled and the descriptors are
# bound to the class attributes, we can inspect the class
# and set proper storage names to the descriptors
# so we need to set the storage name when the class is created,
# that can be done with a class decorated of metaclass.
# decorator is the easier way, as will show here
@model.entity
class LineItem:
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    potato = LineItem('potato', 10, 9)
    print(potato.__dict__)
    # {'_NonBlank#description': 'potato', '_Quantity#weight': 10, '_Quantity#price': 9}
    # this is what we want
