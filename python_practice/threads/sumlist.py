import threading

list1 = [range(10000)]
list2 = [range(10000, 20000)]
list3 = [range(20000, 30000)]

def process(l):
    print("Calculating sum")
    print(f"Sum = {sum(l)}")
    print("Calculated sum")


def main():
    thread1 = threading.Thread(target=process, args=list1)
    thread2 = threading.Thread(target=process, args=list2)
    thread3 = threading.Thread(target=process, args=list3)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
    
    print("DONE")

main()