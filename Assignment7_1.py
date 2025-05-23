# Write two lambda functions:- One to calculate square of a number.
#                            - Another to calculate cube of a number.


ChkSquare = lambda a:a*a
ChkCube = lambda b : b * b * b

no1=int(input("Enter a number : "))

ret1 = ChkSquare(no1)
ret2 = ChkCube(no1)

print("Square is : ",ret1)
print("Cube is : ",ret2)


