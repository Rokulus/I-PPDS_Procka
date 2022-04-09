# 7. Exercise
This is a documentation for the seventh exercise from the subject I-PPDS.

# Application
Aplication is generating numbers until the limit is reached.
-   First program ***generate_number*** is generating numbers.
-   Second program ***check_odd_even*** is checking if number is odd or even.
-   Third program ***prime_number*** is checking if number is a prime number. When ***close*** function is called the program writes out how many times number was a prime number.

There is one scheduler that controls alternation between 3 tasks.

# Scheduler
Scheduler holds list of co-programs.
-   ***Add*** function which adds program to the list of programs. It invokes the ***next*** function so that the next program can wait for ***yield*** function.
-   ***Start*** function starts tasks. Each task is in alternation in while cycle. When exception is called the start function close each task with ***close*** function.

# Printout

![Bad Release](https://raw.githubusercontent.com/Rokulus/I-PPDS_Procka/07/images/printout.png)
