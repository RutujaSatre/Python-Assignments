# Write a program which contains one lambda function which accept one parameter and return power of two.

ChkPower = lambda x:x**2

print("Enter number : ")
ret=int(input())

num=ChkPower(ret)
print("Power is : ",num)
