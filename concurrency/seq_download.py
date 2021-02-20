import os
import sys
import time

import requests

IMAGE_NAMES = ('y5OZxH y5OAPO y5OVRe y5OFIK y5Oia6 y5OEGD y5OmMd y5OnsA y5OMZt y5OuqI').split()  # <2>

BASE_URL = 'https://imgchr.com/i/'

DEST_DIR = 'downloads/'


def save_img(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_img(cc):
    url = '{}/{cc}/{cc}.png'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def download_many(img_list):
    for img in sorted(img_list):
        image = get_img(img)
        show(img)
        save_img(image, img.lower())

    return len(img_list)


def main(download_many):
    t0 = time.time()
    count = download_many(IMAGE_NAMES)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main(download_many)
