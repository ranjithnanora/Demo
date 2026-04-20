import asyncio
import time

async def add_num(num1,num2):
    print("Performing additions")
    await asyncio.sleep(2)
    print(f"Addition: {num1+num2}")
    return num1+num2

async def sub_num(num1,num2):
    print("Performing subtraction")
    await asyncio.sleep(5)
    print(f"subtraction: {num1-num2}")
    return num1-num2

async def mul_num(num1,num2):
    print("Performing multiplication")
    await asyncio.sleep(1)
    print(f"multiplication: {num1*num2}")
    return num1*num2

def end(future):
    try:
        print(future)
        print("calculation complete")
        print(future.result())
    except Exception:
        time.sleep(6)

async def main(num1,num2):
    """
    gather will continue execution even if one task throws exception remaining task will continue run
    but the wait function will exit due to exception
    :param num1:
    :param num2:
    :return:
    """
    try:
        task=asyncio.gather(sub_num(num1,num2), add_num(num1,num2), mul_num(num1,None) )
        print(task)
        #await task
        task.add_done_callback(end)
        await task
        #print(task)
    except Exception as e:
        print(e)
        await asyncio.sleep(6)

async def main2(num1,num2):
    """
    taskgroup stop all remaining execution when exception is raised
    :param num1:
    :param num2:
    :return:
    """
    try:
        async with asyncio.TaskGroup() as task_group:
                task_group.create_task(sub_num(num1, num2))
                task_group.create_task(add_num(num1,None))
                task_group.create_task(mul_num(num1,num2))
    except Exception as e:
        print(e)
        await asyncio.sleep(6)



asyncio.run(main(5,3))
asyncio.run(main2(2,1))