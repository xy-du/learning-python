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

# nested tuple unpacking
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.00000000)),
]
print('{:15}|{:^9}|{:^9}'.format('', 'lat', 'long'))
fmt = '{:15}|{:^9.4f}|{:^9.4f}'  # here : means space control 9 means width and .4 means precision
for name, cc, pop, (latitude, longitude) in metro_areas:
    print(fmt.format(name, latitude, longitude))
