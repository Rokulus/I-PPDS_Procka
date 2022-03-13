"""
Jakub Prôčka
Nuclear Power Plant #2
"""
from random import randint
from time import sleep
from fei.ppds import Thread, Semaphore, Mutex, Event


class LightSwitch():
    def __init__(self):
        self.count = 0
        self.M = Mutex()

    def lock(self, sem):
        self.M.lock()
        counter = self.count
        self.count += 1
        if self.count == 1:
            sem.wait()
        self.M.unlock()
        return counter

    def unlock(self, sem):
        self.M.lock()
        self.count -= 1
        if self.count == 0:
            sem.signal()
        self.M.unlock()


def init():
    access_data = Semaphore(1)
    turniket = Semaphore(1)
    ls_monitor = LightSwitch()
    ls_cidlo = LightSwitch()
    valid_data = Event()

    for monitor_id in range(8):
        Thread(monitor, monitor_id, valid_data, turniket, ls_monitor,
               access_data)
    for cidlo_id in range(3):
        Thread(cidlo, cidlo_id, turniket, ls_cidlo, valid_data, access_data)


def monitor(monitor_id, valid_data, turniket, ls_monitor, access_data):
    valid_data.wait()

    while True:
        """Read should be non stop so there is no sleep"""
        turniket.wait()
        turniket.signal()

        pocet_citajucich_monitorov = ls_monitor.lock(access_data)
        trvanie_citania = randint(40, 50)/1000

        print(f'monit "{monitor_id:02d}": '
              f'pocet_citajucich_monitorov={pocet_citajucich_monitorov:02d}'
              f'trvanie_citania={trvanie_citania:5.3f}')
        ls_monitor.unlock(access_data)


def cidlo(cidlo_id, turniket, ls_cidlo, valid_data, access_data):
    while True:
        """Actualization"""
        sleep(randint(50, 60)/1000)

        turniket.wait()

        pocet_zapisujucich_cidiel = ls_cidlo.lock(access_data)

        if cidlo_id == 2:
            """This is entry of sensor H"""
            trvanie_zapisu = randint(20, 25)/1000
        else:
            """This is entry of sensor P and T"""
            trvanie_zapisu = randint(10, 20)/1000

        turniket.signal()

        print(f'cidlo "{cidlo_id:02d}": '
              f'pocet_zapisujucih_cidiel={pocet_zapisujucich_cidiel:02d}, '
              f'trvanie_zapisu={trvanie_zapisu:5.3f}')
        sleep(trvanie_zapisu)

        """It is unlocked here because monitors can read older news from
            sensors. If we would signal valida_data here
            (as in Nuclear Power Plant #1) the monitors would wait
            for every sensor to finish it's job."""
        ls_cidlo.unlock(access_data)

        """Last sensor did it's job"""
        valid_data.signal()


if __name__ == '__main__':
    init()
