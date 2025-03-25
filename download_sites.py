import os
import threading
import urllib.request
import time
from concurrent.futures import ThreadPoolExecutor

def download_site(url):
    print("Stahujem..."+url)
    with urllib.request.urlopen(url) as response:
        print(f"Stiahnutie {url}: {len(response.read())} bytov")

sites = [
    "http://www.example.com",
    "http://www.example.org",
    "http://www.example.net",
    "http://www.google.com",
    "http://www.httpforever.com",
    "https://www.sme.sk",
]

threads = []
start_time = time.time()

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = []
    for site in sites:
        futures.append(executor.submit(download_site, site))

    for future in futures:
        result = future.result()

duration = time.time() - start_time
print(f"Stiahnuté {len(sites)} stránok za {duration} sekúnd")

print(os.cpu_count())