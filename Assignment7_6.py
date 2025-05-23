# Write a function that accepts a list of integers and returns a list of all prime numbers using filter().

ChkPrime = lambda no :no > 1 and all(no % i != 0 for i in range(2, int(no**0.5) + 1))

def main():

    print("Enter a List : ")
    num = list(map(int,input().split()))

    FData = list(filter(ChkPrime,num))
    print("Prime Numbers : ",FData)



if __name__=="__main__":
    main()