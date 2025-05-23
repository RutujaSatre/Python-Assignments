# Accept a list of integer from the user and use  the map() function to double each value.

value = lambda a : a*2


print("Enter List : ")
val = list(map(int,input().split()))

MData = list(map(value,val))
print("Value: ",MData)

