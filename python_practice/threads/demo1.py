import threading
import time 

def task1():
    print("Task started")
    time.sleep(3)
    print("Task completed")

def task2():
    time.sleep(1)
    print("Task2 started")
    time.sleep(2)
    print("Task2 completed")


thread = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)
thread.start()
thread2.start()
thread.join()
thread2.join()
print("The main thread's execution is completed")