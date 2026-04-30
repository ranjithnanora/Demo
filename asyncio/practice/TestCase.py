import asyncio
import time
from HybridExecutor import HybridExecutor

# IO Task (async)
async def fetch_url(url):
    await asyncio.sleep(1)
    return f"Fetched: {url}"


# IO Task (failure)
async def fetch_fail(url):
    await asyncio.sleep(1)
    raise ValueError("Invalid URL")


# CPU Task
def factorial(n):
    if n < 0:
        raise ValueError("Negative number")
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


# CPU Task (slow)
def slow_task(n):
    time.sleep(2)
    return f"Done {n}"

executor = HybridExecutor()

executor.add_task("io", fetch_url, "https://example.com")
executor.add_task("cpu", factorial, 5)
executor.add_task("cpu", slow_task, 5)
executor.add_task("io", fetch_fail, "https://example.com")
results = asyncio.run(executor.run())
print(results)