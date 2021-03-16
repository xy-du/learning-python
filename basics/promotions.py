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
