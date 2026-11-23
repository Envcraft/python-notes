# Level 6 - Topic 5: Concurrency
# Running multiple tasks "at the same time"

import threading
import time

# --- Threading: best for I/O-bound tasks (file, network) ---
def download_file(name, duration):
    print(f"Starting download: {name}")
    time.sleep(duration)  # simulate network wait
    print(f"Finished download: {name}")

# Without threading: sequential (slow)
start = time.time()
# download_file("file1.txt", 2)
# download_file("file2.txt", 2)
# Total: ~4 seconds

# With threading: concurrent (fast)
t1 = threading.Thread(target=download_file, args=("file1.txt", 1))
t2 = threading.Thread(target=download_file, args=("file2.txt", 1))

start = time.time()
t1.start()
t2.start()
t1.join()  # wait for t1 to finish
t2.join()  # wait for t2 to finish
print(f"Threading total: {time.time() - start:.2f}s")  # ~1s not 2s

# --- Asyncio: modern way for async I/O ---
import asyncio

async def fetch_data(name, delay):
    print(f"Fetching {name}...")
    await asyncio.sleep(delay)  # non-blocking wait
    print(f"Got {name}!")
    return f"data from {name}"

async def main():
    # Run both concurrently
    results = await asyncio.gather(
        fetch_data("API 1", 1),
        fetch_data("API 2", 1),
    )
    print(results)

asyncio.run(main())

# --- Multiprocessing: CPU-bound tasks (actual parallel execution) ---
from multiprocessing import Pool

def cpu_work(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        results = pool.map(cpu_work, [1_000_000] * 4)
    print(f"Results: {results[:2]}...")
