# Write a recursive function to print the following  pattern: (Right Triangle)
#           *
#           **
#           ***
#           ****


def pattern(no,no1=1):
    if no1 > no:
        return
    print("*"*no1)

    pattern(no,no1+1)


def main():
    pattern(4)

if __name__=="__main__":
    main()
