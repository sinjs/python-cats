"""
This script will download a lot of cats into the cats folder in the directory this script is executed
The cats folder must exist.
"""

from multiprocessing import Pool, freeze_support
import os
import time
import requests

api_url = "https://nekos.life/api/v2/img/meow"
output = "cats"


def get_cat_url() -> str:
    resp = requests.get(api_url)
    data = resp.json()
    return data["url"]


def download_cat(url: str):
    filename = url.rsplit('/', 1)[1]
    outpath = os.path.join(output, filename)
    if os.path.exists(outpath):
        return outpath
    resp = requests.get(url, allow_redirects=True)
    open(outpath, "wb").write(resp.content)
    return outpath


def download_cats(amount: int):
    for i in range(1, amount):
        print(f"{i}: {download_cat(get_cat_url())}")


def run_multiprocessing(func, i, n_processors):
    with Pool(processes=n_processors) as pool:
        return pool.map(func, i)


def main():
    start = time.process_time()
    num_max = 100
    n_processors = 6
    x_ls = list(range(num_max))
    run_multiprocessing(download_cats, x_ls, n_processors)
    print("time: {} seconds\n".format((time.process_time()-start)))


if __name__ == "__main__":
    freeze_support()
    main()
