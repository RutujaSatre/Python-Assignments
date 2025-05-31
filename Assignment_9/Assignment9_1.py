# Create a python program that starts 3 threads , each printing numbers from 1 to 5 with delay of 1 second . Use threading.Thread.

import threading
import time

def thread1():
    for i in range(1,6):
        print(i)
        time.sleep(1)

def thread2():
    for i in range(1,6):
        print(i)
        time.sleep(1)

def thread3():
    for i in range(1,6):
        print(i)
        time.sleep(1)

def main():
    T1 = threading.Thread(target = thread1) 
    T1.start()
    T1.join()

    T2 = threading.Thread(target = thread2) 
    T2.start()
    T2.join()

    T3 = threading.Thread(target = thread3)
    T3.start()   
    T3.join()


if __name__=="__main__":
    main()