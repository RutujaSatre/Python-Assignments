# Accept a list of number and use filter() to keep only even numbers.

ChkEven = lambda no : (no%2==0)

print("Enter no of elements: ")
Size= list(map(int,input().split()))

FData=list(filter(ChkEven,Size))
print("Filter Output: ",FData)

