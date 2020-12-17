# tuple can be seen as: 1.immutable list 2.records with no field name

# tuple as record. note that the order of the items in the tuple can not be changed, or it will lose information
cordinate = (12.212121, 10.12121212)  # one record
city, year, pop, pch, area = ('hangzhou', 2020, 1000, 0.1, 23000)  # one record. unpacking
travelor_ids = [('USA', '7984746829'), ('CHA', '7482927432'), ('UK', '64839274649')]  # a collection of record
for passport in travelor_ids:
    print('%s:%s' % passport)  # unpacking

for country, _ in travelor_ids:
    print(country)

# parallel assignment
lat, long = cordinate
print(lat)
print(long)
# elegent swap
a = 1
b = 2
a, b = b, a
print(a, b)

# prefix an argument with star.
print(divmod(10, 4))
t = (10, 4)
print(divmod(*t))  # get the same answer

# enable function to return multiple value in a way that is convenient to the caller
import os

_, filename = os.path.split('/duxingyu/desktop/test.cpp')
print(filename)

# use * to grab excess items
a, b, *rest = range(5)
print((a, b, rest))
a, *rest, b = range(5)
print((a, b, rest))
a, b, c, d, *rest = range(5)
print((a, b, c, d, rest))
a, b, c, d, e, *rest = range(5)
print((a, b, c, d, e, rest))
