# make sure run this file with terminal instead of pycharm 'Run xx.py' option,
# so that you can see the differences

import sys
import time

# python use buffer by default, the default value of 'end' parameter
# of print is '\n' that will trigger the flush, so you can see the numbers
# one by one in this example
for i in range(5):
    print(i)
    time.sleep(0.3)

print('##############')

# when you change the end, there is no more default flush, so buffer mechanism
# come in, so you do not see the numbers one by one, but all at once when the
# the last number is produced
for i in range(5):
    print(i, end=' ')
    time.sleep(0.3)

print('\n##############')

for i in range(5):
    print(i, end=' ')
    sys.stdout.flush()
    time.sleep(0.3)

print('\n##############')

for i in range(5):
    print(i, flush=True, end=' ')
    time.sleep(0.3)
