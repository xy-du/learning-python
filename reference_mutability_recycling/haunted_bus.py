class HauntedBus:
    def __init__(self, passenger=[]):
        self.passenger = passenger

    def drop(self, *name):
        for n in name:
            self.passenger.remove(n)

    def pick(self, *name):
        for n in name:
            self.passenger.append(n)


hb1 = HauntedBus(['aaa', 'bbb'])
hb1.pick('ccc')
print(hb1.passenger)

hb2 = HauntedBus()
hb2.pick('h11', 'h22', 'h33')
print(hb2.passenger)

hb3 = HauntedBus()
hb3.pick('b11')
print(hb3.passenger)
# wired things happen here, the passenger in hb3 turn out to be the same with hb2, but is not the same with hb1
print(hb1.passenger)

print(hb1.passenger is hb2.passenger)
print(hb2.passenger is hb3.passenger)
# the cat is out of the bag now, since both bh2 and hb3 are created with no initial passengers, the refer to the
# the same attribute of the function object
# each default value is evaluated when the function is defined, (i.e., usually when the module is loaded),and the
# default value become attributes of the function objects, so if it is a mutable object and you change it, the change
# will affect every future call of the function.
# This also explains why None is used as the default value for parameters that may receive mutable values.

print('__defaults__' in dir(HauntedBus.__init__))  # you can find __defaults__ here
print(HauntedBus.__init__.__defaults__[0] is hb2.passenger)  # and you can the these two are identical
