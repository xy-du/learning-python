def quantity():
    try:
        quantity.counter += 1
    except AttributeError:
        quantity.counter = 0

    storage_name = '_{}#{}'.format('quantity', quantity.counter)

    def qyt_getter(instance):
        return instance.__dict__[storage_name]

    def qyt_setter(instance, value):
        if value > 0:
            setattr(instance, storage_name, value)
        else:
            raise ValueError('value must be > 0')

    return property(qyt_getter, qyt_setter)


class ItemLine:
    weight = quantity()
    price = quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    it = ItemLine('banana', 10, 10)
    print(it.subtotal())

    it = ItemLine('potato', -10, 10)  # this will cause error
    print(it.subtotal())
