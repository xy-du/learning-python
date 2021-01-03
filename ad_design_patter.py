from collections import namedtuple
from abc import ABC, abstractmethod

Customer = namedtuple('Customer', 'name fedility')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            # discount = self.promotion.discount(self)
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):  # technically, __repe__ is used to print 'official' info that can even used to reconstruct obj
        fmt = '<Order total: {:.2f} due: {:.2f}>'  # {:[.precision][type]}
        return fmt.format(self.total(), self.due())


class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """return discount as a positive dollar amount"""


# class FidelityPromo(Promotion):
#     """5% discount for customers with 1000 or more fedility points"""
#
#     def discount(self, order):
#         return 0.05 * order.total() if order.customer.fedility else 0
#
# class BulkItemPromo(Promotion):
#     """%10 discount for each lineitem with 20 or more units"""
#
#     def discount(self, order):
#         discount = 0
#         for item in order.cart:
#             if item.quantity > 20:
#                 discount += item.total() * 0.1
#         return discount
#
#
# class LargeOrderPromo(Promotion):
#     """%7 discount for orders with 10 or more distinct items"""
#
#     def discount(self, order):
#         distinct_items = {lineitems.product for lineitems in order.cart}
#         if len(distinct_items) >= 10:
#             return order.total() * 0.07
#         return 0

def fidelity_promo(order):
    """5% discount for customers with 1000 or more fedility points"""
    return 0.05 * order.total() if order.customer.fedility >= 1000 else 0


def bulkitem_promo(order):
    """%10 discount for each lineitem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


def large_order_promo(order):
    """%7 discount for orders with 10 or more distinct items"""
    distinct_item = {item.product for item in order.cart}
    if len(distinct_item) >= 10:
        return order.total() * 0.07
    return 0


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]
banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)]
long_order = [LineItem(str(prod_code), 1, 1.0) for prod_code in range(10)]

# pass in FidelityPromo() instead of FidelityProme, do not confuse class with function
# FidelityPromo() means it's an instance of the class
# print(Order(joe, cart, fidelity_promo))
# print(Order(ann, cart, fidelity_promo))
# print(Order(joe, banana_cart, bulkitem_promp))
# print(Order(joe, long_order, large_order_promo))

# to choose the best strategy, here is the simple approach
# you should get used to the first-class feature of the functions in python, then it's nature to building data structure
# that hold functions as its element

# promos = [fidelity_promo, bulkitem_promp, large_order_promo]
promos = [globals()[name] for name in globals()
          if name.endswith('_promo')
          and name != 'best_promos']
print(promos)


# this is indeed a simple approach
# BUT, what if you have a new promotion strategy? you have to manually code it into the list, or it can only be used
# when pass as a argument into Order
def best_promo(order):
    return max(promo(order) for promo in promos)


print(Order(joe, long_order, best_promo))
print(Order(joe, banana_cart, best_promo))
print(Order(ann, cart, best_promo))
