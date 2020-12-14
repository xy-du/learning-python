import test

print('here is main.py. __name__ = ',__name__)
if(__name__=='__main__'):
    print('test.py is running directly')
else:
    print('test.py is running by others')