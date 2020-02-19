import time

COUNT = 50000000


def countdown(n):
    while n > 0:
        n -= 1


if __name__ == "__main__":
    start_time = time.time()

    countdown(COUNT)

    total_time = time.time() - start_time

    print(f"TIME OF EXECUTION IS {total_time} SEC")
