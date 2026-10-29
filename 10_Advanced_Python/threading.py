import threading
import time

def worker(name):
    for i in range(2):
        print(name, i)
        time.sleep(0.1)

threads = [threading.Thread(target=worker, args=(name,)) for name in ("A", "B")]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("Threads finished")
