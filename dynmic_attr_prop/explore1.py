import keyword
from collections import abc


class FrozenJSON:
    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):  # in case the key is a python keyword, which is invalid
                key += '_'
            elif not str.isidentifier(key):
                pass  # some logic to deal invalid identifier
            self.__data[key] = value

    def __getattr__(self, item):
        if hasattr(self.__data, item):
            return getattr(self.__data, item)
        else:
            return FrozenJSON.build(self.__data[item])  # KeyError will happen here if item is not in the keys

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return FrozenJSON(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [FrozenJSON.build(item) for item in obj]
        else:
            return obj


if __name__ == '__main__':
    from osconfeed import load

    feed = load()
    fj = FrozenJSON(feed)

    print(len(fj.Schedule.speakers))
    print(sorted(fj.Schedule.keys()))
    for key, value in sorted(fj.Schedule.items()):
        print('{:3} {}'.format(len(value), key))

    print(fj.Schedule.speakers[-1].name)
    talk = fj.Schedule.events[40]
    print(type(talk))
    print(talk.name)
    print(talk.speakers)
    # print(talk.flavor)  # this one will has a KeyError
