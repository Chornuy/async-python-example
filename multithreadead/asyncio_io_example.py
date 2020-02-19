import asyncio
import time
import aiohttp

URL_LIST = [
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


async def download_image(session, filename, url):
    async with session.get(url) as response:
        with open(f"assets/{filename}.jpg", "wb") as fh:
            data = await response.read()
            fh.write(data)


async def download_all_images(url_list):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in url_list:
            task = asyncio.ensure_future(download_image(session, url.split("/")[-1], url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":

    start_time = time.time()
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(download_all_images(URL_LIST))
    total_time = time.time() - start_time
    print(f"EXECUTION TIME {total_time} MS")

"0.25072503089904785"
