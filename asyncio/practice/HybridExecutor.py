import asyncio
import threading
from functools import wraps


# Unified logging decorator
def track_task(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        print(f"[START] {func.__name__}")
        print(f"Thread: {threading.current_thread().name}")

        try:
            result = await func(*args, **kwargs)
            print(f"[SUCCESS] {func.__name__}")
            return {"task": func.__name__, "status": "SUCCESS", "result": result}
        except Exception as e:
            print(f"[FAILED] {func.__name__} -> {e}")
            return {"task": func.__name__, "status": "FAILED", "error": str(e)}

    return wrapper


class HybridExecutor:
    def __init__(self):
        self.cpu_tasks = []
        self.io_tasks = []

    def add_task(self, task_type, func, *args):
        if task_type == "io":
            self.io_tasks.append(func(*args))  # coroutine
        elif task_type == "cpu":
            self.cpu_tasks.append((func, args))
        else:
            raise ValueError("Invalid task type")

    @track_task
    async def run_cpu_task(self, func, *args):
        return await asyncio.to_thread(func, *args)

    @track_task
    async def run_io_task(self, coro):
        return await coro

    async def run(self):
        results = []

        # Run CPU tasks concurrently
        cpu_futures = [
            self.run_cpu_task(func, *args)
            for func, args in self.cpu_tasks
        ]

        # Run IO tasks concurrently
        io_futures = [
            self.run_io_task(coro)
            for coro in self.io_tasks
        ]

        # Run everything together
        all_tasks = cpu_futures + io_futures

        if all_tasks:
            results = await asyncio.gather(*all_tasks)

        return results