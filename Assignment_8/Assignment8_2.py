# Design python application which creates two threads as evenfactors and oddfactors. Both the thread accept one parameter as integer . Evenfactor thread will display addition of even factor of given number and oddfactor will display addition of odd factors of given number. After execution of both the thread gets completed main thread should display message as "exit from main".

import threading

def evenfactor(no):
    sum = 0
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 == 0:
            sum = sum+i
    print(f"Sum of even factors of {no}: ",sum)


    
def oddfactor(no):
    sum = 0
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 != 0:
            sum =sum + i
    print(f"Sum of odd factors of {no}: ",sum)


def main():
    print("Enter number : ")
    num = int(input())

    T1 = threading.Thread(target=evenfactor,args=(num,))
    T1.start()
    T1.join()

    T2 = threading.Thread(target = oddfactor,args=(num,))
    T2.start()
    T2.join()


    print("Exit from main")

if __name__=="__main__":
    main()