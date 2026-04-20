import asyncio
""" 
.run()  This is your entry point.
.create_task( func()) Schedules a coroutine to run in the background. func() is async function
.gather() Run many coroutines at once and wait for all of them.
.sleep() 
.wait() More control than gather
.asyncio.to_thread() Run normal (blocking) functions without freezing async code.
.get_running_loop() Gives access to: scheduling callbacks, low-level control
Synchronization:
        asyncio.Lock()
        asyncio.Event()
        asyncio.Semaphore()

"""
print(dir(asyncio))