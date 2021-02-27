def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))


def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))


class Overriding:
    """a.k.a. data descriptor or enforced descriptor"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)  # <2>

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverridingNoGet:
    """an overriding descriptor without ``__get__``"""

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class NonOverriding:
    """a.k.a. non-data or shadowable descriptor"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):
        print('-> Managed.spam({})'.format(display(self)))


if __name__ == '__main__':
    # NOTE:
    # normally, Reading an attribute through an instance returns
    # the attribute defined in the instance, but if there is no
    # such attribute in the instance, a class attribute will be retrieved.
    # On the other hand, assigning to an attribute in an instance normally
    # creates the attribute in the instance, without affecting the class at all.
    # but with descriptor, the situation become complicated
    # A descriptor that implements the __set__ method is called
    # an overriding descriptor, because although it is a class
    # attribute, a descriptor implementing __set__ will override
    # attempts to assign to instance attributes
    # if the descriptor has both __set__ and __get__, both read and write
    # through the instance will get interrupted (override)
    # ALL in ALL,
    # if there is __set__, it will get in the way when you set the value of the namesake
    # attribute. But, if there is __get__, weather or not it will be invoked depended on
    # that if the instance can find the attribute with that name in itself, say instance.attr1,
    # if a attribute named 'attr1' can not be found, then the __get__ will get invoked
    print('-----------------overriding descriptor------------------')
    obj = Managed()
    print(obj.over)
    print(Managed.over)
    obj.over = 7
    print(vars(obj))
    print(obj.over)
    obj.__dict__['over'] = 8
    print(vars(obj))
    print(obj.over)

    # without the __get__, when you try to read the attribute through the
    # instance, it will not get overridden, but the write process still will
    print('---------overriding descriptor without __get__---------------')
    print(obj.over_no_get)
    print(Managed.over_no_get)
    obj.over_no_get = 7
    print(obj.over_no_get)
    print(Managed.over_no_get)
    obj.__dict__['over_no_get'] = 9
    print(obj.over_no_get)  # instance attribute shadow the descriptor
    print(Managed.over_no_get)
    obj.over_no_get = 7
    print(obj.over_no_get)  # still 9, instance attribute still shadow the descriptor

    # when there is no __set__, when you create the attribute on the instance, it will
    # not get overridden
    print('-----------------Nonoverriding descriptor------------------')
    obj = Managed()
    print(obj.non_over)
    print(Managed.non_over)
    obj.non_over = 7
    print(vars(obj))
    print(obj.non_over)
    print(Managed.non_over)
    del obj.non_over
    print(obj.non_over)

    print('----------override the descriptor in the class------------------')
    obj = Managed
    Managed.over = 1
    Managed.over_no_get = 2
    Managed.non_over = 3
    print(obj.over, obj.over_no_get, obj.non_over)  # the descriptors are all gone
    # Regardless of whether a descriptor is overriding or not,
    # it can be overwritten by assignment to the class.
    # This is a monkey-patching technique
    # reveals another asymmetry regarding reading and writing attributes:
    # although the reading of a class attribute can be controlled
    # by a descriptor with __get__ attached to the managed class,
    # the writing of a class attribute cannot be handled by a descriptor
    # with __set__ attached to the same class (that would require metaclass tech)

    print('-------------methods are descriptor')
    obj = Managed()
    print(obj.spam)  # <bound method Managed.spam of <__main__.Managed object at 0x109c0bd00>>
    print(Managed.spam)  # <function Managed.spam at 0x108e501f0>
    obj.spam = 23
    print(obj.spam)  # 23 shadows the class attribute, rendering the spam method inaccessible from the obj instance.
    print(Managed.spam)
