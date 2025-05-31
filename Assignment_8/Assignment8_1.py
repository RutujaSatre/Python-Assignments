# Design python application which creates two thread named as even and odd. Even thread will display first 10 even numbers and odd thread will display first 10 odd numbers

import threading

def Even():
    for i in range(2,21,2):
        print(i)

def Odd():
    for i in range(1,20,2):
        print(i)

def main():
    print("Even numbers")
    T1 = threading.Thread(target=Even)
    T1.start()
    T1.join()

    print("Odd numbers")
    T2 = threading.Thread(target=Odd)
    T2.start() 
    T2.join()


if __name__=="__main__":
    main()
