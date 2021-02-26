def quantity(storage_name):
    def qyt_getter(instance):
        return instance.__dict__[storage_name]

    def qyt_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError('Value must be > 0')

    return property(qyt_getter, qyt_setter)


class LimeItem:
    weight = quantity('weight')
    price = quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    lt = LimeItem('banana', 10, 20)
    print(lt.subtotal())

    lt = LimeItem('potato', -10, 20)  # this will cause the ValueError
    print(lt.subtotal())
