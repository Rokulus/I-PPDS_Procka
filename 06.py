"""
Jakub Prôčka
Barber shop
"""

from fei.ppds import Thread, Mutex, Semaphore
from time import sleep
from random import randint

number_of_customers = 10


class Shared:
    def __init__(self):
        """We want that customer wait for barber and barber wait for customer
           and we want them to start at the same time. That's why we
           use Semaphore for them."""
        self.customer = Semaphore(0)
        self.barber = Semaphore(0)
        """We want from customer to say when he is ok with his haircut.
           And he needs to wait for barber to finish his job."""
        self.customerDone = Semaphore(0)
        self.barberDone = Semaphore(0)
        """We want only one customer to get haircut at the time.
           So we need mutex for that."""
        self.gettingHaircut = Mutex()

        """Barber shop."""
        self.waitingCustomers = 0
        self.barberShop_capacity = 5
        self.barberShop_mutex = Mutex()
        self.queue = []

    def enter_barberShop(self, customer_id):
        if self.waitingCustomers == self.barberShop_capacity:
            print(f'Barber Shop is Full. Customer {customer_id} is leaving.\n')
        if self.waitingCustomers < self.barberShop_capacity:
            self.barberShop_mutex.lock()
            print(f'Customer {customer_id} is waiting.\n')
            self.queue.append(customer_id)
            self.waitingCustomers += 1
            self.barberShop_mutex.unlock()

    def leave_barberShop(self, customer_id):
        self.barberShop_mutex.lock()
        print(f'Customer {customer_id} left Barber Shop.\n')
        self.waitingCustomers -= 1
        self.queue.pop(0)
        self.barberShop_mutex.unlock()


def customer(customer_id, shared):
    while True:
        sleep(randint(1, 100) / 100)
        shared.enter_barberShop(customer_id)

        if customer_id not in shared.queue:
            """Customer can't get a haircut if he's not in barbershop."""
            continue

        shared.gettingHaircut.lock()
        shared.customer.signal()
        shared.barber.wait()

        print(f'Customer {customer_id} is getting haircut.\n')
        sleep(randint(50, 200) / 100)

        shared.customerDone.signal()
        print(f'Customer {customer_id} is finished.\n')
        shared.barberDone.wait()
        shared.gettingHaircut.unlock()

        shared.leave_barberShop(customer_id)


def barber(shared):
    while True:
        shared.customer.wait()
        shared.barber.signal()

        print(f'Barber doing haircut.\n')
        sleep(randint(50, 200) / 100)

        shared.customerDone.wait()
        shared.barberDone.signal()
        print(f'Barber finished doing haircut.\n')


def main():
    shared = Shared()

    customers = []
    barber_employee = Thread(barber, shared)

    for i in range(number_of_customers):
        customers.append(Thread(customer, i, shared))

    for t in customers:
        t.join()
    barber_employee.join()


if __name__ == "__main__":
    main()
