import queue
import threading 

def producer(q):
    for item in range(5):  # Producing 5 items
        print(f"Produced: {item}")
        q.put(item)
    q.put(None)  # Termination signal

def consumer(q):
    while True:
        item = q.get()
        if item is None:  # Termination condition
            break
        print(f"Consumed: {item}")


q = queue.Queue()
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
q.put(None)
consumer_thread.join()
print("Thread communication completed")