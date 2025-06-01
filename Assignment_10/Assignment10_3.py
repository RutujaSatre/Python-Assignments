# Write a program which contain filter(),map() and reduce() in it.Python application which contains one list of numbers.List contains the numbers which are accepted from user.Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.Map function will increase each numbers by 10.Reduce will return product of all that numbers.


from functools import reduce

Numbers = lambda no : no>=70 and no<=90
Increase = lambda no : no+10
Product = lambda no1,no2 : no1*no2


print("Enter List : ")
Data = list(map(int,input().split()))

FData = list(filter(Numbers,Data))
print("Filter output: ",FData)

MData = list(map(Increase,FData))
print("Map Output: ",MData)

RData = reduce(Product,MData)
print("Reduced Output : ",RData)


