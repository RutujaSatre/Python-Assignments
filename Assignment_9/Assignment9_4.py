# Create a python program that Compare execution time of summing numbers from 1 to 10 million using normal function, threading, and multiprocessing.

import time
import threading
import multiprocessing

def normal(value):
    total = 0
    for i in range(1, value + 1):
        total = total + i
    return total

def threads(value):
    total = 0
    for i in range(1, value + 1):
        total = total + i
    return total

def process(value):
    total = 0
    for i in range(1, value + 1):
        total =total +  i
    return total

def main():
    value = 10000000

    start_time = time.time()
    normal(value)
    end_time = time.time()
    print("Normal function time: ",end_time - start_time, "seconds")

    start_time = time.time()
    thread = threading.Thread(target=threads, args=(value,))
    thread.start()
    thread.join()
    end_time = time.time()
    print("Threading time: ",end_time - start_time,"seconds")

    start_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.apply(process, args=(value,))
    end_time = time.time()
    print("Multiprocessing time: ",end_time - start_time ,"seconds")

if __name__ == '__main__':
        main()