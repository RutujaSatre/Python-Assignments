# Accept 5 numbers from the user . Find and print the largest number

def main():
    
    print("Enter 5 numbers : ")
    num = list(map(int,input().split()))

    for i in range(5):
        val = num[0]

    for i in num:
        if i > val:
            val = i

    print("Largest number : ",val)


if __name__=="__main__":
    main()