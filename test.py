import os
import sys
import time

import requests

POP20_CC = ('p1.png p2.png p3.png p4.png p5.png '
            'p6.png p7.png p8.png p9.png p10.png').split()  # <2>

BASE_URL = 'https://github.com/xy-du/learning-python/blob/concurrency-feature/imgs/'  # <3>

DEST_DIR = 'downloads/'  # <4>


def save_flag(img, filename):  # <5>
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_flag(cc):  # <6>
    url = '{}/{cc}/{cc}.png'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content


def show(text):  # <7>
    print(text, end=' ')
    sys.stdout.flush()


def download_many(cc_list):  # <8>
    for cc in sorted(cc_list):  # <9>
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower())

    return len(cc_list)


def main():  # <10>
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main()
