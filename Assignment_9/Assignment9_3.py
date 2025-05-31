# Create a python program that uses multiprocessing . Pool to compute factorial of numbers in a list.

import multiprocessing

def factorial(no):
    ans = 1
    for i in range(1,no+1):
        ans = ans*i
    return ans


def main():
    list = [1,2,3,4,5]

    P = multiprocessing.Pool()
    result = P.map(factorial,list)  
    print(result)  


if __name__=="__main__":
    main()