# 4. Exercise
This is a documentation for the fourth exercise from the subject I-PPDS.

The base of the code is taken from Nuclear Power Plant #1 exercise in [4. cvičenie – Večerajúci filozofi, Atómová elektráreň](https://uim.fei.stuba.sk/i-ppds/4-cvicenie-vecerajuci-filozofi-atomova-elektraren-%f0%9f%8d%bd%ef%b8%8f/).


# Pseudocode

        def init():
            accessData = Semaphore(1)
            turniket = Semaphore(1)
            ls_monitor = Lightswitch()
            ls_cidlo = Lightswitch()
            validData = Event()

            // we got 8 monitors
            for monitor_id in range(8):
                create_and_run_thread(monitor, monitor_id)
            // we got 3 sensors
            for cidlo_id in range(3):
                create_and_run_thread(cidlo, cidlo_id)

        def monitor(monitor_id):
            // Monitor can't work, unless there is at least 1 valid data in storage
            validData.wait()

            while True:
                //Read of monitors should be non stop so there is no sleep implemented
                turniket.wait()
                turniket.signal()

                // Gain access to storage
                pocet_citajucich_monitorov = ls_monitor(accessData).lock()
                trvanie_citania = rand(40 to 50 ms)

                // Access to data by simulating following print
                print('monit "%02d":
                      pocet_citajucich_monitorov=%02d\n
                      trvanie_citania=%5.3f')
                sleep(trvanie_citania)
                // Data was updated, we can now leave a storage
                ls_monitor(accessData).unlock()

        def cidlo(cidlo_id):
            while True:
                // Actualization
                sleep(50 to 60 ms)

                turniket.wait()
                // Gain access to storage
                pocet_zapisujucich_cidiel = ls_cidlo(accessData).lock()

                // We got 3 sensors (H,T,P). Sensor H write 20 to 25ms and T,P sensors
                // write 10 to 20 ms. So we need IF condition to seperatem them.
                if cidlo_id == 2:
                    trvanie_zapisu = rand(20 to 25 ms)
                else:
                    trvanie_zapisu = rand(10 to 20 ms)
                turniket.signal()

                // Access to data by simulating following print
                print('cidlo "%02d":
                      pocet_zapisujucich_cidiel=%02d,               trvanie_zapisu=%03d\n')
                sleep(trvanie_zapisu)

                // Monitors can work only if all of th sensors did it's job so we
                // unlock them after that.
                ls_cidlo(accessData).unlock()

                // Last sensor did it's job so we can signal that data are valid.
                validData.signal()

# Printout
![Bad Release](https://raw.githubusercontent.com/Rokulus/I-PPDS_Procka/04/images/power_plant2.png)
