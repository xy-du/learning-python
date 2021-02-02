class Demo:
    @classmethod
    def clsmethod(*args):
        return args

    @staticmethod
    def staticmethod(*args):
        return args


if __name__ == '__main__':
    print(Demo.clsmethod())
    print(Demo.clsmethod('abc'))
    print(Demo.staticmethod())
    print(Demo.staticmethod('abc'))

# as you can see, classmethod always pass the Class itself as the first argument, but staticmethod does not
# do this.

# classmethod
#   define a method that is operate on the class instead of the instance, it's commonly used for alternative
#   constructor

# staticmethod
#   it is just like a plain function that happens to live in a class body, instead of being defined at the
#   module level
