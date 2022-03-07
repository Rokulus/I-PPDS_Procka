from random import randint
from time import sleep
from fei.ppds import Thread, Semaphore, Mutex
from typing import Callable
import matplotlib.pyplot as plt


class LightSwitch():
    def __init__(self):
        self.count = 0
        self.M = Mutex()

    def lock(self, sem):
        self.M.lock()
        if not self.count:
            sem.wait()
        self.count += 1
        self.M.unlock()

    def unlock(self, sem):
        self.M.lock()
        self.count -= 1
        if not self.count:
            sem.signal()
        self.M.unlock()


class Shared():
    def __init__(self, N):
        self.finished = False
        self.M = Mutex()
        self.free = Semaphore(N)
        self.items = Semaphore(0)
        self.count = 0


def producer(shared, produce: Callable[[], float]):
    while True:
        """production"""
        sleep(produce())
        """control of free space in storage"""
        shared.free.wait()
        if shared.finished:
            break
        """gain access to storage"""
        shared.M.lock()
        """save product in storage"""
        shared.count += 1
        """leave storage"""
        shared.M.unlock()
        """increase number of products in storage"""
        shared.items.signal()


def consumer(shared, consume: Callable[[], float]):
    while True:
        """control content of storage"""
        shared.items.wait()
        if shared.finished:
            break
        """gain access to storage"""
        shared.M.lock()
        """gain product from storage"""
        shared.free.signal()
        """leave storage"""
        shared.M.unlock()
        """consume product"""
        sleep(consume())


def main():
    storage = 20
    producers = 10
    graph = []

    for produce in range(10):
        for consumers in range(1, 11):
            items_sum = 0
            j = 10
            for i in range(j):
                shared = Shared(storage)
                x = 100
                [Thread(consumer, shared, lambda: randint(0, 10) / x) for i in range(consumers)]
                [Thread(producer, shared, lambda: produce / x) for i in range(producers)]

                sleep_time = 0.05
                sleep(sleep_time)
                shared.finished = True
                shared.items.signal(100)
                shared.free.signal(100)

                produced = shared.count
                items = produced / sleep_time
                items_sum += items
            items_sum_average = items_sum / j
            graph.append((produce / x, consumers, items_sum_average))

    plot(graph)


def plot(graph: list):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    x = [a[0] for a in graph]
    y = [a[1] for a in graph]
    z = [a[2] for a in graph]
    ax.set_xlabel('Time to produce (s)')
    ax.set_ylabel('Number of Consumers')
    ax.set_zlabel('Number of products per second')
    ax.plot_trisurf(x, y, z, cmap='magma')
    plt.show()


if __name__ == "__main__":
    main()
