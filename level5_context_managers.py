# Level 5 - Topic 3: Context Managers
# Manage resources (files, connections) automatically
# "with" statement ensures cleanup even if errors occur

# Most common: file handling
with open("temp_example.txt", "w") as f:
    f.write("Hello, file!\n")
    f.write("Second line.\n")
# File is automatically closed here, even if an error occurred

with open("temp_example.txt", "r") as f:
    content = f.read()
    print(content)

# Custom context manager using a class
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        print("Timer started.")
        return self  # available as "as" variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        elapsed = time.time() - self.start
        print(f"Timer stopped. Elapsed: {elapsed:.4f}s")
        return False  # don't suppress exceptions

with Timer() as t:
    total = sum(range(1_000_000))
    print(f"Sum: {total}")

# Custom context manager using contextlib (simpler)
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f"Opening {name}")
    try:
        yield name  # pauses here while inside "with" block
    finally:
        print(f"Closing {name}")  # always runs

with managed_resource("database") as db:
    print(f"Using {db}")
# Opening database
# Using database
# Closing database

# Clean up temp file
import os
os.remove("temp_example.txt")
