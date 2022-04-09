"""
Jakub Prôčka
7. exercise
"""
from random import randint


class Scheduler():
    def __init__(self):
        self.tasks = list()

    def add(self, task):
        next(task)
        self.tasks.append(task)

    def start(self):
        value = 0
        while True:
            try:
                task = self.tasks.pop(0)
                value = task.send(value)
                self.tasks.append(task)
            except StopIteration:
                for i in self.tasks:
                    i.close()
                break


def generate_number(stop):
    limit = 0
    number = 0
    count = 0
    while True:
        limit += (yield number)
        if limit > stop:
            print("="*10)
            print(f'Sum {limit} is higher than {stop}')
            print(f'Count of numbers generated: {count}')
            break
        number = randint(2, 100)
        count += 1
        print(f'Generating {number}')


def check_odd_even():
    number = 0
    while True:
        number = (yield number)
        if number % 2 == 0:
            print(f'{number} is even')
        else:
            print(f'{number} is odd')


def prime_number():
    number = 0
    count = 0
    flag = False
    while True:
        try:
            number = (yield number)
            flag = False
            for i in range(2, number):
                if (number % i) == 0:
                    flag = True
                    break
            if flag:
                print(f'{number} is not a prime number')
            else:
                count += 1
                print(f'{number} is a prime number')
        except GeneratorExit:
            print(f'Number of times when number was a prime number: {count}\n')
            return


limit = 100
app = Scheduler()
app.add(generate_number(limit))
app.add(check_odd_even())
app.add(prime_number())
app.start()
