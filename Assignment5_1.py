# Write a program to accept two integers from the user and display their: Sum, Difference, Product, Division.

def main():
    print("Enter First numbers : ")
    no1=int(input())

    print("Enter Second number : ")
    no2=int(input())

    sum=no1+no2
    difference=no1-no2
    product=no1*no2
    division=no1/no2

    print("Sum : ",sum)
    print("Difference : ",difference)
    print("Product : ",product)
    print("Division : ",division)


if __name__=="__main__":
    main()