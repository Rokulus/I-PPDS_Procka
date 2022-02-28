from fei.ppds import Thread, Mutex, Semaphore, Event
from random import randint
from time import sleep


class SimpleBarrier:
    def __init__(self, N):
        self.N = N
        self.C = 0
        self.M = Mutex()
        self.T = Event()
    
    def only_one(self, thread_id):
        """This function secures that each thread
           goes after one another like this: 0-1-2-3-...
        """
        while self.C != self.N:
            """We check if the wanted thread is doing job
               right now. If it does then it increases
               counter, set Event and then go out of the function.
               If not, then it goes to wait.
            """
            if self.C == thread_id:
                self.M.lock()
                self.C += 1
                self.T.set()
                self.M.unlock()
                return
            self.T.wait()


def compute_fibonacci(sb1, thread_id):
    sleep(randint(1,10,)/10)
    sb1.only_one(thread_id)
    fib_seq[thread_id+2] = fib_seq[thread_id] + fib_seq[thread_id+1]


THREADS = 10
fib_seq = [0] * (THREADS + 2)
fib_seq[1] = 1

sb1 = SimpleBarrier(THREADS)

threads = [Thread(compute_fibonacci, sb1, i) for i in range(THREADS)]

[t.join() for t in threads]
print(fib_seq)