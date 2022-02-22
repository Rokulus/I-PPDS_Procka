from collections import Counter
from time import sleep
from random import randint
from fei.ppds import Thread, Mutex


class Shared():
    def __init__(self, size):
        self.counter = 0
        self.end = size
        """
        Size is increased to prevenet index out of range.
        """
        self.elms = [0] * (size + 1)


def do_count(shared):
    while shared.counter < shared.end:
        mutex.lock()
        shared.elms[shared.counter] += 1
        """
        Sleep command is too make a wanted mistake with array that we try
        to fix with mutex.
        """
        sleep(randint(1, 10)/1000)
        shared.counter += 1
        mutex.unlock()


mutex = Mutex()
shared = Shared(1_00)
t1 = Thread(do_count, shared)
t2 = Thread(do_count, shared)
t1.join()
t2.join()

counter = Counter(shared.elms)
print(counter.most_common())
