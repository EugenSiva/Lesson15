import threading
import time

def print_message(message):
    for i in range(5):
        time.sleep(1)
        print(message + "-" + str(i+1))

thread1 = threading.Thread(target=print_message, args=("Vlákno 1 beží",))
thread2 = threading.Thread(target=print_message, args=("Vlákno 2 beží",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Vlákna ukončili vykonávanie.")