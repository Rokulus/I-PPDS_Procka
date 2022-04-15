"""
Jakub Prôčka
08 async
"""
import time
import asyncio
from aiohttp import ClientSession


async def jokes(names):
    x = names.split()
    async with ClientSession() as session:
        async with session.get('http://api.icndb.com/jokes/random?firstName='
                               + x[0] + '&lastName=' + x[1]) as response:
            print_json(await response.json())


def print_json(data):
    print('==========')
    print('Joke: ', data['value']['joke'])
    print('Categories of the joke: ', data['value']['categories'])
    print('==========')


async def main():
    names = ['jozko paprika', 'peto zemiak', 'miso uhorka', 'palo paradajka']

    start = time.time()
    await asyncio.gather(*(jokes(name) for name in names))
    end = time.time()
    print('Time elapsed:', end - start)

if __name__ == '__main__':
    asyncio.run(main())
