# Although often used as a decorator, the property built-in is
# actually a class. In Python, functions and classes are often
# interchangeable, because both are callable and there is no new
# operator for object instantiation, so invoking a constructor
# is no different than invoking a factory function. And both can
# be used as decorators, as long as they return a new callable that
# is a suitable replacement of the decorated function.

# All arguments are optional, and if a function is not provided for one of them, the cor‐
# responding operation is not allowed by the resulting property object.

# The classic form is better than the decorator syntax in some situations.
# On the other hand, in a class body with many methods, the decorators make
# it explicit which are the getters and setters, without depending on the
# convention of using get and set prefixes in their names.
class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight  # here the property setter is already in use here
        self.price = price

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError('value must be > 0')

    def subtotal(self):
        return self.price * self.weight

    weight = property(get_weight, set_weight)


if __name__ == '__main__':
    lt = LineItem('Potato', 10, 10)
    print(lt.subtotal())

    # now try to set the weight with a negative value will cause an error
    lt = LineItem('Tomato', -10, 10)
    # lt.set_weight(-20)
    print(lt.subtotal())
