# Accept a number from the user check and whether it is prime or not.

def main():
    print("Enter a number : ")
    no = int(input())

    if no > 1:
        for i in  range(2,no):
            if(no % i==0):
                print("It is not a prime : ",no)
                break
        else:
                print("It is a prime number : ",no)

if __name__=="__main__":
    main()

