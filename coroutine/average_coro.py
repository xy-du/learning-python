def average():
    cnt = 0
    total = 0.0
    ave = None
    while True:  # only terminate when call .close() on it, or by GC when no reference to it
        x = yield ave
        total += x
        cnt += 1
        ave = total / cnt


if __name__ == '__main__':
    ave = average()
    next(ave)  # priming
    print(ave.send(10))
    print(ave.send(20))
    print(ave.send(30))
