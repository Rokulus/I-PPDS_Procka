# 5. Exercise
This is a documentation for the fifth exercise from the subject I-PPDS.

The base of the code is taken from Savages #1 exercise in [5. cvičenie – Problém fajčiarov, problém divochov](https://uim.fei.stuba.sk/i-ppds/5-cvicenie-problem-fajciarov-problem-divochov-%f0%9f%9a%ac/).

# Analysis
Diffrence from Savages #1 is that now we have more cooks. When savage finds out that pot is empty he have to inform **ALL** of the cooks that pot is empty. And when pot is full only **ONE** cooks informs savages that pot is full.

I used Event() for the signalization of empty_pot because we want all of the cooks begin cooking.

Savages are waiting for each other to begin eating. Savage then send information how many portions are in the pot and takes the portion and begins eating. This is in cycle unless the pot is empty. When the pot is empty, savages makes signal that pot is empty and they wait for the pot to be full again.

Cooks are on the waiting line and wait for savages to make announcement that pot is empty. When they get the signal, the pot_is_full is set to false and they begin cooking. When last one finishes cooking he make annoucement that all cooks finished cooking and writes out how many servings are in the pot. After that the first cook (the first one that makes it to mutex) adds M portions to pot, signal savages that pot is full, set pot_is_full to True (so that other cooks don't do the same thing over again) and clears the empty_pot Event. Then all of the cooks wait in the line in empty_pot (they wait again until the pot is empty).

# Pseudocode
        // N - number of savages, M - number of portions, C - number of cooks
        N = 5
        M = 20
        C = 5

        class SimpleBarrier(object)
            def __init__(self, N):
                self.N = N
                self.cnt = 0
                self.mutex = Mutex()
                self.varrier = Semaphore(0)
            // Wait for each other
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

            // Event that pot is empty. It is Event because we want to let all
            // of the cooks begin cooking.
            self.empty_pot = Event()
            self.full_pot = Semaphore(0)
            // Announcement from one cook to savages that pot is full.
            self.pot_is_full = False

            self.b1 = SimpleBarrier(N)
            self.b2 = SimpleBarrier(N)
            self.bc = SimpleBarrier(C)

        // Savages eating
        def eat(i):
            print(savage i eating)
            sleep(time to eat)

        def savage(i, shared):
            sleep(time to recover from eating)
            while True:
                shared.b1.wait()
                shared.b2.wait(each=savage i:  is on the line for dinner',
                              last=savage i: all of us are here')

                shared.mutex.lock()
                print(savage i: number of portions: shared.servings)
                if shared.servings == 0:
                    print(savage i: pot is empty)
                    // Signal that pot is empty so all cooks start cooking.
                    shared.empty_pot.signal()
                    // Wait for the pot to be full.
                    shared.full_pot.wait()
                print(savage i : takes from pot)
                shared.servings -= 1
                shared.mutex.unlock()
                eat(i)

        def cook(i, shared):
            while True:
                shared.empty_pot.wait()
                shared.pot_is_full = False
                print(cook i: cooking)
                sleep(randint(time to cook)

                // Last cook make announcement that all cooks finished cooking.
                shared.bc.wait(last=cook i: all cooks finished cooking and made M portions')
                // Here only ONE cook wakes up savages that pot is full.
                shared.mutexC.lock()
                if not shared.pot_is_full:
                    // Add servings to pot.
                    shared.servings += M
                    // Signal savages that pot is full.
                    shared.full_pot.signal()
                    shared.pot_is_full = True
                    shared.empty_pot.clear()
                shared.mutexC.unlock()

# Printout
![Bad Release](https://raw.githubusercontent.com/Rokulus/I-PPDS_Procka/05/images/savages2.png)
