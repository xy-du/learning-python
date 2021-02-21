import collections
from concurrent import futures

import requests
import tqdm

from concurrency.seq_download_2 import main, download_one, HTTPStatus


# NOTE:
#   building a dict to map each future to other data that may be
# useful when the future is completed.
#   Calling the result method on a future either returns the value
# returned by the callable, or raises whatever exception was
# caught when the callable was executed. This method may block
# waiting for a resolution, but not in this example because as_completed
# only returns futures that are done.
#   when the iterable tqdm take has no len, you have to give it one manually
#

def download_many(img_list, verbose):
    counter = collections.Counter()
    img_list = sorted(img_list)
    todo_map = {}
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        for img_name in img_list:
            ft = executor.submit(download_one, img_name)
            todo_map[ft] = img_name
        done_iter = futures.as_completed(todo_map)
        if not verbose:
            done_iter = tqdm.tqdm(done_iter, total=len(img_list))
        for future in done_iter:
            try:
                res = future.result()
            except requests.exceptions.HTTPError as exc:
                resp = exc.response
                error_msg = f'Http error {resp.status_code} - {resp.content}'
                status = HTTPStatus.error
            except requests.exceptions.ConnectionError as exc:
                error_msg = 'connect error'
                status = HTTPStatus.error
            else:
                error_msg = ''
                status = res.status
            if error_msg and verbose:
                print(error_msg)
            counter[status] += 1
    return counter


if __name__ == '__main__':
    main(download_many)
