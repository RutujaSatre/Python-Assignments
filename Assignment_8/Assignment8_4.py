# Design python application which create three threads as small, capital, digits.All the threads accepts  string as parameter .Small thread display number of small characters,capital thread display number of capital characters and digits thread display number of digits.Display id and name of each thread.

import threading
import os

def Small(string):
    count=0
    for i in string:
        if i.islower():
            count=count+1
    print("ID  : ",os.getpid(),"Thread Name : Small Thread ","Count : ",count)

def Capital(string):
    count=0
    for i in string:
        if i.isupper():
            count=count+1
    print("ID : ",os.getpid(),"Thread Name : Capital Thread ","Count : ",count)

def Digits(string):
    count=0
    for i in string:
        if i.isdigit():
            count=count+1
    print("ID : ",os.getpid(),"Thread Name : Digits Thread ","Count : ",count)
        

def main():
    string = "JaiGanesh001"

    T1 = threading.Thread(target=Small,args=(string,))
    T1.start()
    T1.join()

    T2 = threading.Thread(target=Capital,args=(string,))
    T2.start()
    T2.join()

    T3 = threading.Thread(target=Digits,args=(string,))
    T3.start()
    T3.join()

if __name__=="__main__":
    main( )