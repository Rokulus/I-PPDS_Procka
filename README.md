# 2. Exercise
This is a documentation for the second exercise from the subject I-PPDS. 

The base of my code is coming from seminar [2021-02 [seminár] Turniket, bariéra](https://www.youtube.com/watch?v=vIiHVcb3HqU&ab_channel=Paraleln%C3%A9programovanieadistribuovan%C3%A9syst%C3%A9my).

# Simple Barrier - 1. exercise
In the first exercise out task was to implement barrier according to the specification from the lecture [2022-02 [prednáška] Mutex, multiplex, rendezvous, bariéra](https://www.youtube.com/watch?v=sR5RWW1uj5g&ab_channel=Paraleln%C3%A9programovanieadistribuovan%C3%A9syst%C3%A9my).

At first we were tasked to use barrier. This is done in this [commit](https://github.com/Rokulus/I-PPDS_Procka/commit/00747b80d9ddcf7fad95cc89e74572f420f9ff57).

Then we were tasked to redone the code with Event instead of Semaphore. So I changed Semaphore for Event. The diffrence with Event is that when event.set is used, all of the threads are free to go. So I still needed the counter.
Definition of the function wait: 
- The counter is increased by one
- It is checked if counter is equeal to the number of threads. If is then event.set() is called and all of the threads are good to go
- I used mutex when the event.wait() is called. If I would not use mutex the threads would left as they pleased but when I did they left as they came (they came like: 0-1-2-3 and they left the same way 0-1-2-3)

# Reusable Barrier - 2. exercise

Second exercise was to use barrier in cycle. 

The first solution with Sempahore is used from seminar. 

The main goal was to rewrite program with Event instead of Semaphore. In this solution I used clear functionaly of Event which set Event all over again. I defined clear function for SimpleBarrier that just calls Event.clear(). The wait function is defined same as from the first exercise where we used simple barrier. 

The main event was to decide where to put the event.clear function. I clear barrier 2 after barrier 1 and barrier 1 after barrier 2 and code functionality works. 
It goes like:
- The threads print "before barrier".
- They all wait for each other in barrier 1. 
- After all printed out "before barrier", the barrier 2 is cleared and they print out "after barrier".
- They wait for each other at the barrier 2. 
- After all printer out "after barrier", the barrier 1 is cleared and they can start the cycle all over again.  

# Fibonacci - 3. exercise

I managed to solved this only with Event and Mutex. 

I tried many diffrent things with Semaphore but none seems to work for me. Some solutions worked but only when I used to print thread_id (for example, it could print anything and it worked) inside the function. I did not used print from fei.ppds module so I don't really get why it worked there. **I have to study more about semaphore**. 

To answer questions from Exercise:
1. What is the smallest number of synchronization objects (semaphores, mutexes, events) needed to solve this task?
- I managed to solve this with using one Event and one Mutex. 
2. Which of the adopted synchronization patterns (mutual exclusion, signaling, rendezvous, barrier) can (reasonably) be used in solving this problem? Specifically describe how the synchronization pattern is used in your solution.
- The base of the code is taken from the seminar. My function "only_one" goes like this:
    - I want to achieve that each thread is doing fibonacci after one another and they have to go after one another like this: 0-1-2-3-4-5-6-7-8-9-... So each thread have a spesific thread_id which the function takes as an argument.
    - In class SimpleBarrier I have self.C . I use this as an counter to achieve that each thread goead after one another.
    - The While cycle checks if all of the threads already did it's job.
    - The If checks if it's the turn of the wanted thread base on the counter. 
        - If it's not then thread is going to wait. 
        - If it is then it's locked and counter is increased and all of the previous thread are unlocked (Event is set). And thread leave the function.   


