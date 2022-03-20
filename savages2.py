"""
Jakub Prôčka
Savages #2
"""
from fei.ppds import Semaphore, Mutex, Thread, print, Event
from random import randint
from time import sleep

"""
N - number of savages
M - number of portions
C - number of cooks
"""
N = 5
M = 20
C = 5


class SimpleBarrier(object):
    def __init__(self, N):
        self.N = N
        self.cnt = 0
        self.mutex = Mutex()
        self.barrier = Semaphore(0)

    def wait(self, each=None, last=None):
        self.mutex.lock()
        self.cnt += 1
        if each:
            print(each)
        if self.cnt == self.N:
            if last:
                print(last)
            self.cnt = 0
            self.barrier.signal(self.N)
        self.mutex.unlock()
        self.barrier.wait()


class Shared(object):
    def __init__(self, m):
        self.servings = m
        self.mutex = Mutex()
        self.mutexC = Mutex()

        """Event that pot is empty. It is Event because we want to
           let all of the cooks begin cooking."""
        self.empty_pot = Event()
        self.full_pot = Semaphore(0)
        """Announcement from one cook to savages that pot is full."""
        self.pot_is_full = False

        self.b1 = SimpleBarrier(N)
        self.b2 = SimpleBarrier(N)
        """Barrier for cooks."""
        self.bc = SimpleBarrier(C)


def eat(i):
    print(f'savage {i}: eating')
    sleep(randint(50, 200) / 100)


def savage(i, shared):
    sleep(randint(1, 100) / 100)
    while True:
        shared.b1.wait()
        shared.b2.wait(each=f'savage {i}: before dinner',
                       last=f'savage {i}: all of us are here')

        shared.mutex.lock()
        print(f'savage {i}: number of portions: {shared.servings}')
        if shared.servings == 0:
            print(f'savage {i}: empty_pot')
            """"Signal that pot is empty so all cooks start cooking."""
            shared.empty_pot.signal()
            """Wait for the pot to be full."""
            shared.full_pot.wait()
        print(f'savage {i}: take from pot')
        shared.servings -= 1
        shared.mutex.unlock()
        eat(i)


def cook(i, shared):
    while True:
        shared.empty_pot.wait()
        shared.pot_is_full = False
        print(f'cook {i}: cooking')
        sleep(randint(50, 200) / 100)

        """Last cook make annoucment that all cooks finished cooking.
        """
        shared.bc.wait(last=f'cook {i}: all finished cooking and {M} servings --> pot')
        """Here only ONE cook wakes up savages that pot is full.
           The pot_is_full secures (with mutex) that only one cook
           makes the waking up.
        """
        shared.mutexC.lock()
        if not shared.pot_is_full:
            """Add servings to pot."""
            shared.servings += M
            """Signal savages that pot is full."""
            shared.full_pot.signal()
            shared.pot_is_full = True
            shared.empty_pot.clear()
        shared.mutexC.unlock()


def main():
    shared = Shared(0)
    savages = []
    cooks = []

    for i in range(N):
        savages.append(Thread(savage, i, shared))

    for i in range(C):
        cooks.append(Thread(cook, i, shared))

    for t in savages + cooks:
        t.join()


if __name__ == '__main__':
    main()
