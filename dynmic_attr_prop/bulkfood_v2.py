class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight  # here the property setter is already in use here
        self.price = price

    @property
    def weight(self):
        return self.__weight

    # decorated getter has a .setter attribute, which is also a decorator,
    # this is how the getter and setter get tied
    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError('value must be > 0')

    def subtotal(self):
        return self.price * self.weight


if __name__ == '__main__':
    lt = LineItem('Potato', 10, 10)
    print(lt.subtotal())

    # now try to set the weight with a negative value will cause an error
    lt = LineItem('Tomato', -10, 10)
    print(lt.subtotal())
