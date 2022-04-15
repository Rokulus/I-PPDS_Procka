"""
Jakub Prôčka
08 sync
"""
import time
import json
import urllib.request as r
from urllib.error import HTTPError


def jokes(names):
    try:
        x = names.split()
        data = r.urlopen('http://api.icndb.com/jokes/random?firstName=' + x[0]
                         + '&lastName=' + x[1]).read()
        print_json(json.loads(data))
    except HTTPError:
        pass


def print_json(data):
    print('==========')
    print('Joke: ', data['value']['joke'])
    print('Categories of the joke: ', data['value']['categories'])
    print('==========')


if __name__ == '__main__':
    names = ['jozko paprika', 'peto zemiak', 'miso uhorka', 'palo paradajka']

    start = time.time()
    for name in names:
        jokes(name)
    end = time.time()
    print('Time elapsed:', end - start)
