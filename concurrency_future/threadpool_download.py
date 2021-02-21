from concurrent import futures

from concurrency_future.seq_download import get_img, save_img, main, show

MAX_WORKS = 20


def download_one(img_name):
    img_cont = get_img(img_name)
    show(img_name)
    save_img(img_cont, img_name.lower())
    return img_name


# the map() method is like the map built-in function, except the
# function here will be called concurrently from multiple thread,
# and it returns generator that can be iterated over to retrieve
# the value returned by each function
def download_many(img_names):
    workers = min(MAX_WORKS, len(img_names))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(img_names))
    # if any of the threaded calls raise an exception, the exception would be
    # raised here as the implicit next() call tried to retrieve the corresponding
    # return value from the iterator
    return len(list(res))


if __name__ == '__main__':
    main(download_many)
