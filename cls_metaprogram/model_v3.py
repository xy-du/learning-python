import abc


class AutoStorage:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        cls_name = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(cls_name, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)


class Validated(abc.ABC, AutoStorage):
    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)

    @abc.abstractmethod
    def validate(self, instance, value):
        """return validated value or raise ValueError"""


class Quantity(Validated):
    def validate(self, instance, value):
        if value > 0:
            return value
        else:
            raise ValueError('value must be > 0')


class NonBlank(Validated):
    def validate(self, instance, value):
        value = value.strip()
        if len(value) != 0:
            return value
        else:
            raise ValueError('value can not be empty or blank')


class EntityMeta(type):
    # this method will be called before __init__
    # and the returned value from here will be received by __init__
    # when the metaclass build a new class
    #   it must be class method
    #   it must return a dict
    # NOTE:
    # here we return a ordered dict so the order that attribute appearing
    # in the classed body can be reserved. as you will see in the bulkfood_v8.py
    @classmethod
    def __prepare__(metacls, name, bases):
        return dict()

    def __init__(cls, name, bases, attr_dict):
        cls._field_names = []
        for key, attr in attr_dict.items():
            if isinstance(attr, Validated):
                type_name = type(attr).__name__
                attr.storage_name = '_{}#{}'.format(type_name, key)
                cls._field_names.append(key)
        super().__init__(name, bases, attr_dict)


# This class exists for convenience only: the user of this module
# can just subclass Entity and not worry about EntityMeta—or even be aware of its existence.
class Entity(metaclass=EntityMeta):
    """business entity with validated field"""

    @classmethod
    def field_names(cls):
        for name in cls._field_names:
            yield name
