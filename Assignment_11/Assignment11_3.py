# Write a recursive function to calculate the sum of digits of a numbers.

sum = 1

def Sum(no):
    if no==0:
        return 0
    return (no%10 + Sum(int(no/10)))
     

def main():
    ret = Sum(1234)
    print("Sum of Digits : ",ret)


if __name__=="__main__":
    main()