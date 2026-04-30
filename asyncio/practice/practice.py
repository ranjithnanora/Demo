import asyncio
import aiohttp
from functools import wraps
import datetime


class APIFetchError(Exception):
    def __init__(self):
        super().__init__("APIFetchError: error in fetching API")

def log_execution(func):
    async def wrapper(*args, **kwargs):
        print(f"function name: {func.__name__}")
        start = datetime.datetime.now()

        try:
            result = await func(*args, **kwargs)
            print(f"Status: SUCCESS")
            return result
        except Exception as e:
            print(f"Status: FAILED -> {e}")
            raise
        
        finally:
            print(f"Execution time: {datetime.datetime.now() - start}")

    return wrapper

def retry(n, delay):
    def wrapper(func):
        @wraps(func)
        async def fetch_and_retry(*args, **kwargs):
            for i in range(n):
                try:
                    data = await func(*args, **kwargs)
                    if data:
                        return data
                except Exception as e:
                    print(f"Retry {i + 1}/{n} failed: {e}")
                    await asyncio.sleep(delay)

            raise APIFetchError()
        return fetch_and_retry
    return wrapper


class ASyncAPIClient:
    @log_execution
    @retry(3,1)
    async def fetch_data(self, urls):
        async with aiohttp.ClientSession() as session:
            async def fetch(url):
                async with session.get(url) as response:
                    if not response.ok:
                        return ""
                    data = await response.text()
                    return data[0:40]
            tasks = [fetch(url) for url in urls]
            res=await asyncio.gather(*tasks)
            return res


a=ASyncAPIClient()
urls = [
    "https://www.geeksforgeeks.org/python/python-functools-wraps-function/",
    "https://example.com"
]

try:
    result=asyncio.run(a.fetch_data(urls))
    print(result)
except APIFetchError as e:
    print(e)