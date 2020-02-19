import time
from concurrent.futures import ThreadPoolExecutor

import requests


url_list = [
    "https://tpc.googlesyndication.com/simgad/11420184489972006704",
    "https://tpc.googlesyndication.com/simgad/11853567373957177842",
    "https://tpc.googlesyndication.com/simgad/8910544366846388803",
    "https://tpc.googlesyndication.com/simgad/16841331040106462158",
    "https://tpc.googlesyndication.com/pimgad/7507680182959332346",
    "https://tpc.googlesyndication.com/pimgad/3307265324934143265",
    "https://tpc.googlesyndication.com/pimgad/4787063135036623285",
    "https://tpc.googlesyndication.com/pimgad/12666193514253160214",
    "https://tpc.googlesyndication.com/pimgad/14289548025795245748"
]


def download_picture(image_url, name):
    image = requests.get(image_url).content
    with open(f"assets/{name}.jpg", 'wb') as fh:
        fh.write(image)


if __name__ == "__main__":
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=9) as executor:
        tasks = [executor.submit(download_picture, url, url.split('/')[-1]) for url in url_list]
        results = [task.result() for task in tasks]

    total_time = time.time() - start_time
    print(f"TIME OF EXECUTION IS {total_time} SEC")
