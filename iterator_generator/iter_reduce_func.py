# the function here receive an iterable and return a single result
# 'reducing'  'folding'  'accumulating'

# functions like all and any can be implemented with reduce, but
# the built-in version has its optimization: short-circuit, which means
# that if the result has been determined, no further iteration will be preceded

print(all([1, 2, 3]))
print(all([1, 0, 2]))
print(all([]))

print(any([1, 2, 3]))
print(any([1, 0, 2]))
print(any([]))

g = (n for n in [0, 0.0, 5, 2])
print(any(g))
print(next(g))

print('###############3#####')

l = [1, 2, 3]
l1 = reversed(l)
l2 = sorted(l)
# reversed return a generator
print(next(l1))
print(next(l1))
print(next(l1))
# sorted return a new, complete list
print(type(l2))
# list.sort() sort the list in-place
print(l)
l.sort(reverse=True)
print(l)
