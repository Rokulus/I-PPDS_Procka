from random import randint
from time import sleep
from fei.ppds import Thread, Semaphore, Mutex, Event
from fei.ppds import print
 
 
class SimpleBarrier:
    def __init__(self, N):
        self.N = N
        self.C = 0
        self.M = Mutex()
        self.T = Event()
 
    def wait(self):
        self.C += 1
        if self.C == self.N:
            self.C = 0
            self.T.set()
        self.M.lock()
        self.T.wait()
        self.M.unlock()
 
 
def exercise1(barrier, thread_id):
    sleep(randint(1,10)/10)
    print("vlakno %d pred barierou" % thread_id)
    barrier.wait()
    print("vlakno %d po bariere" % thread_id)
 

sb = SimpleBarrier(5)

threads = [Thread(exercise1, sb, i) for i in range(5)]
[t.join() for t in threads]