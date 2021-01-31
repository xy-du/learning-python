import time
from clockdeco2 import clock


@clock
def snooze(sec, aa, bb, cc):
    time.sleep(sec)


snooze(.123, 11, bb=22, cc=22)
