import threading
import time 


def odd():
    for i in range(1, 10, 2):
        print(i)

def even():
    for i in range(2, 10, 2):
        print(i)


thread = threading.Thread(target=odd)
thread2 = threading.Thread(target=even)
thread.start()
thread2.start()
thread.join()
thread2.join()
print("The main thread's execution is completed")