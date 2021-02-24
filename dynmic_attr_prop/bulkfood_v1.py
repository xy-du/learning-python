class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.price * self.weight


if __name__ == '__main__':
    lt = LineItem('Potato', 10, 10)
    print(lt.subtotal())

    # But problem is:
    lt = LineItem('Tomato', -10, 10)
    print(lt.subtotal())
    # negative price, it is unrealistic!!!!
