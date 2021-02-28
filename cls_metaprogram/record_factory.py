# class metaprograming is the art of creating or customizing classes at runtime
# classes are first-class objects in python

# a example is the collections,namedtuple

# before begin:
# about type(): we usually think it as a function, but it's actually a class,
# which can take three arguments(name,bases,dict) to create a new class,
# just as what you will see in the following example
# i.e., the instance of type are classes
# And, invoke type with three arguments ia s common wway of creating a class
# dynamically

def record_factory(cls_name, field_names):
    try:
        field_names = field_names.replce(',', ' ').split()
    except AttributeError:
        pass
    field_names = tuple(field_names)

    def __init__(self, *args, **kwargs):
        attrs = dict(zip(self.__slot__, args))
        attrs.update(kwargs)
        for key, value in attrs.items():
            setattr(self, key, value)

    def __iter__(self):
        for name in self.__slot__:
            return getattr(self, name)

    def __repr__(self):
        value = ','.join('{}={!r}'.format(*i)
                         for i in zip(self.__slot__, self))
        return '{}({})'.format(self.__class__.__name__, value)

    cls_attrs = dict(__slots__=field_names,
                     __init__=__init__,
                     __repr__=__repr__,
                     __iter__=__iter__)

    return type(cls_name, (object,), cls_attrs)
