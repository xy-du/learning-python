import asyncio
import collections
from enum import Enum

import aiohttp
import tqdm
from aiohttp import web

from concurrency_asyncio.download_asyncio import save_flag, IMAGE_NAMES, BASE_URL


class HTTPStatus(Enum):
    ok = 1
    error = 2
    not_found = 3


Result = collections.namedtuple('Result', 'status,msg')

DEFAULT_CONCUR_REQ = 5


class FetchError(Exception):  # use this to carry some info when things go south
    def __init__(self, country_code):
        self.country_code = country_code


async def get_flag(session, base_url, cc):
    url = '{}/{}.png'.format(base_url, cc)
    async with session.get(url) as resp:
        if resp.status == 200:
            return await resp.read()
        elif resp.status == 404:
            raise web.HTTPNotFound()
        else:
            raise aiohttp.HttpProcessingError(
                code=resp.status, message=resp.reason,
                headers=resp.headers)


async def download_one(session, cc, base_url, semaphore, verbose):
    try:
        async with semaphore:
            image = await get_flag(session, base_url, cc)
    except web.HTTPNotFound:
        status = HTTPStatus.not_found
        msg = 'not found'
    except Exception as exc:
        raise FetchError(cc) from exc
    else:
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, save_flag, image, cc.lower() + '.png')
        # save_flag(image, cc.lower() + '.png')
        status = HTTPStatus.ok
        msg = 'OK'

    if verbose and msg:
        print(cc, msg)

    return Result(status, cc)


async def downloader_coro(cc_list, base_url, verbose, concur_req):
    counter = collections.Counter()
    semaphore = asyncio.Semaphore(concur_req)
    async with aiohttp.ClientSession() as session:
        to_do = [download_one(session, cc, base_url, semaphore, verbose)
                 for cc in sorted(cc_list)]

        to_do_iter = asyncio.as_completed(to_do)
        if not verbose:
            to_do_iter = tqdm.tqdm(to_do_iter, total=len(cc_list))
        for future in to_do_iter:
            try:
                res = await future
            except FetchError as exc:
                country_code = exc.country_code
                try:
                    error_msg = exc.__cause__.args[0]
                except IndexError:
                    error_msg = exc.__cause__.__class__.__name__
                if verbose and error_msg:
                    msg = '*** Error for {}: {}'
                    print(msg.format(country_code, error_msg))
                status = HTTPStatus.error
            else:
                status = res.status

            counter[status] += 1

    return counter


def download_many(cc_list, base_url, verbose, concur_req):
    loop = asyncio.get_event_loop()
    coro = downloader_coro(cc_list, base_url, verbose, concur_req)
    counts = loop.run_until_complete(coro)
    loop.close()

    return counts


if __name__ == '__main__':
    download_many(IMAGE_NAMES, BASE_URL, False, DEFAULT_CONCUR_REQ)
