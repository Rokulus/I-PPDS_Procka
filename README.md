# 1. Exercise
This is a documentation for the first exercise from the subject I-PPDS. 

In this exercise our assignment was to use mutex(below, I will refer to it as lock) to prevent two threads from incrementing one element of the array. 
- Unwanted output:
    - [(1, 99), (2, 1)]
- Wanted output:
    - [(1, 100)]

Each solution is divided in seperate file. Base of the code is taken from [2021-02 [seminár] Úvod do PPaDS, inkrementácia indexu poľa](https://www.youtube.com/watch?v=HNGZJ0MXSWI).

I'am using Python version **3.10**. For making the mistake (which generates unwanted output) I use sleep command (in the code there is an comment for the specified line). The sleep command is to make it so the first element of the array is incremented two times by one with each thread. 

## 01 Solution
For the first solution I use lock in the function do_count() which increment the element of the array. First I lock it before the while cycle so one thread can finish the cycle. After that the lock is unlocked so the other thread can do it's job.

## 02 Solution
In my second solution firstly I tried to use the lock inside the while cycle. This seemed to generete wanted output but index was out of range. So in order to fix this I tried one solution presented in seminar which was to increase size of class Shared. 

This solution works with two numbers:
- Output when size is increased by 1:
    - [(1, 101)]
- Output when size is increased by 2 and operator in while cycle is changed to <= :
    - [(1, 102)]
- Output when size is increased but any other natural number (for example 10):
    - [(1, 102), (0, 8)]

I think it is caused by the condition because condition is already satisfied.

**But for my final version of second solution** I increase size of the class Shared by 1 and I use lock inside the while cycle so I get output [(1, 101)]. 

## 03 Solution
For the third solution I tried to lock each individual line of the while cycle but that gave me only unwanted output. As the last option I use lock before the while cycle and then use unlock before t2 thread can do it's job. I think this solution is similar to the first solution.  


