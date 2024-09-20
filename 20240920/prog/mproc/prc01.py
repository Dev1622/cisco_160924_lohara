import multiprocessing
import os
import time
import threading

lock = threading.lock

def print_numbers():
    pid = os.getpid()
    for i in range(20):
        print(f'{i}@{pid}')
        time.sleep(0.025)
        with lock:
            total = total + 1


if __name__ == '__main__':
    processes = []
    for i in range(5):
        process = multiprocessing.Process(target=print_numbers)
        processes.append(process)
        process.start()
    #for i in range(5):
        #process[i].join()
        #process.join()

    print_numbers()
