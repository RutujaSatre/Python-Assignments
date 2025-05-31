# Design python application which creates two thread as evenlist and oddlist. Both the thread accepts list of integers as parameter.Evenlist thread add all even elements from input list and display the addition. Oddlist thread add all odd elements from input list and display the addition. 

import threading

def evenlist(data):
    sum=0
    for i in data:
        if i%2==0:
            sum=sum+i
    print(sum)

def oddlist(data):
    sum = 0
    for i in data:
        if i%2!=0:
            sum=sum+i
    print(sum)
def main():
    data = [1,2,3,4,5,6]
    result=[]
    print("Addition of Even elements : ")
    T1 = threading.Thread(target = evenlist, args=(data ,))
    T1.start()
    T1.join()

    print("Addition of Odd elements : ")
    T2 = threading.Thread(target = oddlist, args=(data ,))  
    T2.start()
    T2.join()

if __name__=="__main__":
    main()