import collections
import os
import sys
import time
from enum import Enum

import requests
import tqdm

IMAGE_NAMES = ('yotaUe yotd4H yotUED yotB8A yot0Cd yotrvt yotyKP yot6Df yotcb8 yot2VS').split()  # <2>

BASE_URL = 'https://s3.ax1x.com/2021/02/21'

DEST_DIR = 'downloads/'

Result = collections.namedtuple('Result', 'status,msg')


class HTTPStatus(Enum):
    ok = 1
    error = 2
    not_found = 3


def save_img(img, filename):
    path = os.path.join(DEST_DIR, filename + '.png')
    with open(path, 'wb') as fp:
        fp.write(img)


def get_img(cc):
    url = '{}/{}.png'.format(BASE_URL, cc)
    resp = requests.get(url)
    return resp.content


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def download_one(img_name):
    try:
        image = get_img(img_name)
    except requests.exceptions.HTTPError as exc:
        resp = exc.response
        if resp.status_code == 404:
            msg = 'not found'
            status = HTTPStatus.not_found
        else:
            raise
    else:
        save_img(image, img_name)
        status = HTTPStatus.ok
        msg = 'ok'
        # print(img_name, 'ok')
    return Result(status, msg)


# if you want to run on a sorted list, you have to sort the list first
# and the use tqdm.tqdm, because if you sort it after you use tqdm, you would
# just get an new iterable instead of the tqdm object.

# if you output strings in the loop of tqdm object, the output will separate the
# progress bar in many lines instead of one. so if you want there is only one bar
# in one line that kept updated, you should do the output after the loop is done,
# just like the error msg here in this method
def download_many(img_list, verbose):
    counter = collections.Counter()
    img_list = sorted(img_list)
    if not verbose:
        img_list = tqdm.tqdm(img_list)
    for img_name in img_list:
        try:
            download_res = download_one(img_name)
        except requests.exceptions.HTTPError as exc:
            resp = exc.response
            error_msg = f'Http error {resp.status_code} - {resp.content}'
            status = HTTPStatus.error
        except requests.exceptions.ConnectionError as exc:
            error_msg = 'connect error'
            status = HTTPStatus.error
        else:
            error_msg = ''
            status = download_res.status
        if error_msg and verbose:
            print(error_msg)

        counter[status] += 1
    return counter


def main(download_many):
    t0 = time.time()
    counter = download_many(IMAGE_NAMES, False)
    elapsed = time.time() - t0
    print(counter)


if __name__ == '__main__':
    main(download_many)
