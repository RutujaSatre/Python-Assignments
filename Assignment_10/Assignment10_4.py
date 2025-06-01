# Write a program which contain filter(),map() and reduce() in it.Python application which contains one list of numbers.List contains the numbers which are accepted from user.Filter should filter out all such numbers which are even.Map function will calculate its square.Reduce will return addition of all that numbers.


from functools import reduce

CheckEven = lambda no : no%2==0
Square = lambda no : no*no
Addition = lambda no1,no2 : no1+no2


print("Enter List : ")
Data = list(map(int,input().split()))

FData = list(filter(CheckEven,Data))
print("Even Numbers : ",FData)

MData = list(map(Square,FData))
print("Square Numbers : ",MData)

RData = reduce(Addition,MData)
print("Addition of numbers : ",RData)