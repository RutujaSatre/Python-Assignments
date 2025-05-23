# Accept three numbers from the user and print the largest number using nested if-else statement

 
def main():
    print("Enter Three numbers")
    no1 = list(map(int,input().split()))

    for i in range(3):
        val = no1[0]

    for i in no1:
        if i > val:
            val = i

    print("Largest Value : ",val)


if __name__=="__main__":
    main()