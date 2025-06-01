# Write a program which contain filter(),map() and reduce() in it.Python application which contains one list of numbers.List contains the numbers which are accepted from user.Filter should filter out all prime numbers.Map function will multiply each number by 2.Reduce will return Maximum number from  that numbers.

from functools import reduce

def ChkPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

Multiply = lambda no : no*2
Maximum = lambda no1,no2 : no1 if no1>no2 else no2

print("Enter List : ")
Data = list(map(int,input().split()))

FData = list(filter(ChkPrime,Data))
print("Prime Numbers : ",FData)

MData = list(map(Multiply,FData))
print("Multiplication :  ",MData)

RData = reduce(Maximum,MData)
print("Maximum Number : ",RData)