import asyncio
import os
import sys
import time

import aiohttp

IMAGE_NAMES = ('yotaUe yotd4H yotUED yotB8A yot0Cd yotrvt yotyKP yot6Df yotcb8 yot2VS').split()  # <2>

BASE_URL = 'https://s3.ax1x.com/2021/02/21'

DEST_DIR = 'downloads/'


def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


async def get_flag(session, cc):
    url = '{}/{}.png'.format(BASE_URL, cc)
    async with session.get(url) as resp:
        return await resp.read()


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


async def download_one(session, cc):
    image = await get_flag(session, cc)
    show(cc)
    save_flag(image, cc.lower() + '.png')
    return cc


async def download_many(cc_list):
    async with aiohttp.ClientSession() as session:
        res = await asyncio.gather(
            *[asyncio.create_task(download_one(session, cc))
              for cc in sorted(cc_list)])

    return len(res)


def main():
    t0 = time.time()
    count = asyncio.run(download_many(IMAGE_NAMES))
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main()
