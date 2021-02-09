class A:
    def ping(self):
        print('ping-A', self)


class B(A):
    def pong(self):
        print('pong-B', self)


class C(A):
    def pong(self):
        print('pong-C', self)


class D(B, C):
    def ping(self):
        super().ping()
        print('ping-D', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


if __name__ == '__main__':
    d = D()
    d.ping()
    print('*************')
    d.pong()
    print('*************')
    d.pingpong()

    print(D.__mro__)

# Any language implementing multiple inheritance needs to deal with
# potential naming conflicts when unrelated ancestor classes implement
# a method by the same name. This is called the “diamond problem”

# the rule is pretty straightforward
#   1. MRO: Method Resolution Order. Classes have an attribute
#   called __mro__ holding a tuple of references to the superclasses
#   in MRO order, from the current class all the way to the object class,
#   the method is resolved following this order
#   2. The MRO takes into account not only the inheritance graph but also
#   the order in which superclasses are listed in a subclass declaration.
#   eg., the B,C order that D subclass
#   3. it’s also possible, and sometimes convenient, to bypass the MRO
#   and invoke a method on a superclass directly., eg. the C.pong(self)
#   at the end of the pingpong() method in D. Note that when calling an
#   instance method directly on a class, you must pass self explicitly,
#   because you are accessing an unbound method.
