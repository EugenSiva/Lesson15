import threading
import time

# Vytvorenie semaforu s dvomi povoleniami
semaphore = threading.Semaphore(2)

def access_resource(i):
    print(f'Vlákno {i} sa pokúša získať semafor.')
    semaphore.acquire()  # Získať povolenie
    print(f'Vlákno {i} vstúpilo do kritickej sekcie.')
    time.sleep(1)  # Simulácia práce
    print(f'Vlákno {i} odchádza z kritickej sekcie.')
    semaphore.release()  # Uvoľniť povolenie

threads = []

for i in range(10):
    threads.append(threading.Thread(target=access_resource, args=(i,)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()