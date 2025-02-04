import threading
import time 

def daemon_task():
    print("Daemon thread running...")
    time.sleep(1)

daemon_thread = threading.Thread(target=daemon_task, daemon=True)
daemon_thread.start()

time.sleep(5)
print("Main thread exiting")