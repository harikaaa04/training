import threading
import time 

def task(lock):
    with lock:
        print(f"{threading.current_thread().name} has acquired the thread")
        time.sleep(2)
        print(f"{threading.current_thread().name} has acquired the thread")

lock = threading.Lock()
