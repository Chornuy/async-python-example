from concurrent.futures.thread import ThreadPoolExecutor
import time

COUNTDOWN = 50000000


def countdown(n):
    while n > 0:
        n -= 1


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as executor:
        start_time = time.time()
        results = [executor.submit(countdown, COUNTDOWN//2) for _ in range(2)]
        results = [result.result() for result in results]
        total_time = time.time() - start_time

    print(f"TIME OF EXECUTION IS {total_time} SEC")
