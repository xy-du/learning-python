# when n!=+n


import decimal

ctx = decimal.getcontext()
ctx.prec = 40
one_third = decimal.Decimal(1) / decimal.Decimal(3)
print(one_third)
print(one_third == +one_third)
ctx.prec = 28
print(one_third == +one_third)

# each occurrence of the expression +one_third produces
# a new Deci mal instance from the value of one_third,
# but using the precision of the current arithmetic context.

from collections import Counter

ct = Counter('aaabbbcccdddeef')
print(ct)
ct['a'] = -3
ct['d'] = 0
print(ct)
print(+ct)

# for practical reasons, Counter addition discards from the result
# any item with a negative or zero count.
# And the prefix + is a shortcut for adding an empty Counter, therefore
# it produces a new Counter preserving only the tallies that are greater than zero.
