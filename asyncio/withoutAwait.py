import asyncio

async def background_task2():
    print("Background2: Starting a long 10s job...")
    await asyncio.sleep(10)
    print("Background2: I finished!")  # This will NEVER print

async def background_task():
    print("Background: Starting a long 10s job...")
    await asyncio.sleep(10)
    print("Background: I finished!")  # This will NEVER print


async def main():
    # We schedule it, putting it in the "Ready Queue"
    task=asyncio.create_task(background_task())
    #await task
    task2 = asyncio.create_task(background_task2())
    print("Main: I'm done with my work.")
    # We are NOT awaiting background_task.
    # main() finishes RIGHT HERE.
    """
    Even though you didn't await the background task, 
    the event loop gave it exactly one tiny chance to run before closing the shop.
    """
asyncio.run(main())
print("The script has exited.")