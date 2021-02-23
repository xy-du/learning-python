import json
import os
import warnings
from urllib.request import urlopen

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON_LOC = 'data/osconfeed.json'


def load():
    if not os.path.exists(JSON_LOC):
        msg = 'download {} to {}'.format(URL, JSON_LOC)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON_LOC, 'wb') as local:
            local.write(remote.read())
    with open(JSON_LOC) as fp:
        return json.load(fp)


if __name__ == '__main__':
    feed = load()
    print(sorted(feed['Schedule'].keys()))
    for key, value in sorted(feed['Schedule'].items()):
        print('{:3} {}'.format(len(value), key))
    print(feed['Schedule']['speakers'][-1]['name'])
    print(feed['Schedule']['speakers'][-1]['serial'])
    print(feed['Schedule']['events'][40]['name'])
    print(feed['Schedule']['events'][40]['speakers'])
