# Write a program to check whether the entered number is even or odd

def main():
    print("Enter Number : ")
    num = int(input())

    if(num%2==0):
        print(num,"is a even number")

    else:
        print(num,"is an odd number")



if __name__=="__main__":
    main()