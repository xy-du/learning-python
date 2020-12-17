# tuple can be seen as: 1.immutable list 2.records with no field name

# tuple as record. note that the order of the items in the tuple can not be changed, or it will lose information
cordinate = (12.212121, 10.12121212)  # one record
city, year, pop, pch, area = ('hangzhou', 2020, 1000, 0.1, 23000)  # one record
travelor_ids = [('USA', '7984746829'), ('CHA', '7482927432'), ('UK', '64839274649')]  # a collection of record
for passport in travelor_ids:
    print('%s:%s' % passport)

for country, _ in travelor_ids:
    print(country)
