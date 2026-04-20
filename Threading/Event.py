import threading
import time

# Initialize the event (flag is False by default)
start_pistol = threading.Event()

def runner(name):
    print(f"Runner {name} is at the starting line, waiting...")
    start_pistol.wait()  # Blocks here until set() is called
    print(f"Runner {name} is sprinting!")

# Create and start 3 runner threads
for i in range(3):
    threading.Thread(target=runner, args=(i,)).start()

time.sleep(2)  # Simulate some preparation time
print("--- Referee fires the pistol! ---")
start_pistol.set()  # All runners wake up at once