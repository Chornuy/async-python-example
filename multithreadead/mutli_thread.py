import time
from threading import Thread

COUNT = 50000000


def countdown(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    thread1 = Thread(target=countdown, args=(COUNT//2,))
    thread2 = Thread(target=countdown, args=(COUNT//2,))

    start_time = time.time()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    total_time = time.time() - start_time

    print("TIME OF EXECUTION IS " + str(total_time) + " SEC")
