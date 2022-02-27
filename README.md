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


