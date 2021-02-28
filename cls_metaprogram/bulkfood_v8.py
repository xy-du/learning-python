import cls_metaprogram.model_v3 as model


class LineItem(model.Entity):
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
    print(LineItem.field_names())
    for name in LineItem.field_names():
        print(name)
