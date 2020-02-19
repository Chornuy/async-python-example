import time
from multiprocessing.pool import Pool

COUNTER = 50000000


def countdown(n):
    while n > 0:
        n -= 1


if __name__ == "__main__":

    pool = Pool(processes=2)
    start_time = time.time()
    worker1 = pool.apply_async(countdown, [COUNTER//2])
    worker2 = pool.apply_async(countdown, [COUNTER//2])
    pool.close()
    pool.join()
    total_time = time.time() - start_time
    print(f"TIME OF EXECUTION IS {total_time} SEC")
