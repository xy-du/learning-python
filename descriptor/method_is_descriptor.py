#  A function within a class becomes a bound method because all
#  user-defined functions have a __get__ method, therefore
#  they operate as descriptors when attached to a class.


import collections


class Text(collections.UserString):
    def __repr__(self):
        return 'Text({!r})'.format(self.data)

    def __str__(self):
        return self.__repr__()

    def reverse(self):
        return self[::-1]


# RUN the following in console
if __name__ == '__main__':
    word = Text('forward')
    print(word)
    print(word.reverse())
    # by far, everything is ok

    print(word.reverse)  # <bound method Text.reverse of Text('forward')>
    print(Text.reverse.__get__(word))  # same as above
    # Any function is a nonoverriding descriptor. Calling its __get__
    # with an instance retrieves a method bound to that instance.
    print(Text.reverse)  # <function Text.reverse at 0x1053a0e50>
    print(Text.reverse.__get__(None, Text))  # same as abovex
    # Calling the function’s __get__ with None as the instance argument
    # retrieves the function itself.
    print(type(Text.reverse), type(word.reverse))  # one is function, one is method

    # a method call on the class works as a function
    print(Text.reverse(Text('forword')))
    print(list(map(Text.reverse, [(1, 2, 3), [4, 5, 6], 'dxy'])))

    print(word.reverse.__self__)
    # the __self__ hold an reference to the instance on which the method
    # was called
    print(word.reverse.__func__)
    # the __func__ hold the reference to the original function attached to the managed class
