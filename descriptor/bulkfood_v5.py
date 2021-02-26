from descriptor import model


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
    lt = LineItem('banana', 10, 10)
    print(lt.subtotal())

    lt = LineItem('', 10, 10)  # cause error as expected

    lt = LineItem('potato', 10, -1)  # cause error as expected
