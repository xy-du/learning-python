# help() use the __doc__ attribute of the property when
# display the documentation

# When property is deployed as a decorator, the docstring of
# the getter method—the one with the @property decorator itself—is
# used as the documentation of the property as a whole.


class Foo:
    @property
    def bar(self):
        """the bar attribute"""
        return self.__dict__['bar']

    @bar.setter
    def bar(self, value):
        self.__dict__['bar'] = value

# RUN on console
# help(Foo.bar)
# help(Foo)
