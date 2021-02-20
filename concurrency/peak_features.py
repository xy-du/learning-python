# Futures are essential components in the internals of concurrent.futures and of asyncio，
# but you don't always see it

# two class named Feature in Python standard library:
# concurrent.features.Feature
# asyncio.Future

# Feature:
#   Futures encapsulate pending operations so that they can be
#   put in queues, their state of completion can be queried, and
#   their results (or exceptions) can be retrieved when available
# NOTE:
#   you should not create them: let framework do their jobs
#   you should not change the state of a future

# query the state of the feature:
#   done(): nonblocking, return bool to tell you weather the feature
#       has executed or not
#   add_done_callback(): more like to be used, you give it a callable that
#       will get called when the feature is done

# get the result of the work:
#   result(): both concurrent.feature.Feature and asyncio.Feature have it;
#   when the work has been done:
#       result() return the result, which is the same for the two library,
#       or re-raise whatever exception raised during the corresponding work thread.
#   when the work has not been done:
#       for concurrent.feature.Feature:
#           it blocks the caller, and you can set a timeout to make it raise a TimeoutError
#       for asyncio.Feature:
#           it doesn't support the timeout option and the preferred way to get the result is
#           using yield from

# some methods in two library return Feature, others just use Feature in a way that is transparent
# to the users(like the map() we use in seq_concur_feature_download.py).

# as_completed()
# takes a iterable of features and return an
# iterator that yield futures as they are done
# submit()
# schedules the callables and return the features of the pending callables

from concurrent import futures

from concurrency.concur_feature_download import download_one
from concurrency.seq_download import main


# def download_one(img_name):
#     img_cont = get_img(img_name)
#     show(img_name)
#     save_img(img_cont, img_name.lower())
#     return img_name


def download_many(img_list):
    img_list = img_list[:5]
    todo = []
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        for img_name in sorted(img_list):
            future = executor.submit(download_one, img_name)
            todo.append(future)
            msg = 'Schedual for {}:{}'
            print(msg.format(img_name, future))

    results = []
    for future in futures.as_completed(todo):
        res = future.result()
        msg = '{} result:{}'
        print(msg.format(future, res))
        results.append(res)

    return len(results)


if __name__ == '__main__':
    main(download_many)
