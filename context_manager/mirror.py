# context manager object is about to control the with statement,
# just like iterator is behind the scene of for statement

# its designed to simplify the try/finally block, which guarantees
# some critical actions are performed after a block of code

# CM protocol:
# __enter__
# after the start of with statement, __enter__ is invoked on the CMO,
# it can return self, but this is not always the case, what ever returned
# from it is assigned to the target variable in the with statement after the 'as'
# __exit__
# performed on the CMO at the end of the block. NOTE that it's invoked on the CMO,
# not on whatever is returned by the __enter__

class LookingGlass:
    def reverse(self, text):
        self.origin_write(text[::-1])

    def __enter__(self):  # only the self arg
        import sys
        self.origin_write = sys.stdout.write
        sys.stdout.write = self.reverse  # a monkey-patch
        return 'ABCDEFG'  # this will be assigned to the target variable after the 'as'

    # return True to tell interpreter that the exception is handled
    # return None or anything but True, the exception will be propagated
    # exc_type: the exception class
    # exc_val: the exception instance
    # traceback: a traceback object
    # None, None, None will be passed in if all went well
    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.origin_write
        if exc_type is ZeroDivisionError:
            print('do not divide by zero!')
            return True


if __name__ == '__main__':
    with LookingGlass() as what:
        print('this is a test')
        print(what)
    print(what)
    print('test if writer is normal')

    with open('mirror.py') as fp:
        src = fp.read(60)
    print(len(src))
    print(fp)
    print(fp.closed, fp.encoding)
    # this will cause an error
    # after exit with statement, fp is still available and you can access
    # its attribute, but you can not perform I/O on it
    # print(fp.read(60))

    # see how CM works
    cmo = LookingGlass()
    print('before')
    what = cmo.__enter__()
    print('middle')
    print(what)
    cmo.__exit__(None, None, None)
    print('after')
