# Accept age from user and check whether the person is eligible to vote .(Age should be 18 or above)

def main():
    print("Enter your Age : ")
    no = int(input())

    if(no>=18):
        print("Eligible to vote")

    else:
        print("You are not Eligible to vote")


if __name__=="__main__":
    main()