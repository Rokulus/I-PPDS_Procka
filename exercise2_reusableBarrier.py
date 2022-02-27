from random import randint
from time import sleep
from fei.ppds import Thread, Semaphore, Mutex
from fei.ppds import print
 
 
class SimpleBarrier:
    def __init__(self, N):
        self.N = N
        self.C = 0
        self.M = Mutex()
        self.T = Semaphore(0)
 
    def wait(self):
        self.M.lock()
        self.C += 1
        if self.C == self.N:
            self.C = 0
            self.T.signal(self.N)
        self.M.unlock()
        self.T.wait()
 
 
def barrier_example(barrier, thread_id):
    sleep(randint(1,10)/10)
    print("vlakno %d pred barierou" % thread_id)
    barrier.wait()
    print("vlakno %d po bariere" % thread_id)
 

def before_barrier(thread_id):
    sleep(randint(1,10)/10)
    print(f"pred barieriou {thread_id}")


def after_barrier(thread_id):
    print(f"za barieriou {thread_id}")
    sleep(randint(1,10)/10)


def barrier_cycle(b1, b2, thread_id):
    while True:
        before_barrier(thread_id)
        b1.wait()
        b2.wait()
        after_barrier(thread_id)


THREADS = 10
sb1 = SimpleBarrier(THREADS)
sb2 = SimpleBarrier(THREADS)

threads = [Thread(barrier_cycle, sb1, sb2, i) for i in range(THREADS)]
[t.join() for t in threads]