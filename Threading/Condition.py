import threading
import time

items = []
condition = threading.Condition()

def consumer():
    with condition:
        # wait_for is cleaner than a while loop with wait()
        condition.wait_for(lambda: len(items) > 0)
        item = items.pop()
        print(f"Consumed {item}")

def producer():
    time.sleep(1) # Simulate some work
    with condition:
        items.append("Product")
        print("Produced an item")
        condition.notify() # Tell one waiting consumer to wake up

threading.Thread(target=consumer).start()
threading.Thread(target=producer).start()