import os
import sys
import time

import requests



IMAGE_NAMES = ('yotaUe yotd4H yotUED yotB8A yot0Cd yotrvt yotyKP yot6Df yotcb8 yot2VS').split()  # <2>

BASE_URL = 'https://s3.ax1x.com/2021/02/21'

DEST_DIR = 'downloads/'


def save_img(img, filename):
    path = os.path.join(DEST_DIR, filename+'.png')
    with open(path, 'wb') as fp:
        fp.write(img)


def get_img(cc):
    url = '{}/{}.png'.format(BASE_URL, cc)
    resp = requests.get(url)
    return resp.content


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def download_many(img_list):
    for img_name in sorted(img_list):
        image = get_img(img_name)
        show(img_name)
        save_img(image, img_name.lower())

    return len(img_list)


def main(download_many):
    t0 = time.time()
    count = download_many(IMAGE_NAMES)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main(download_many)
