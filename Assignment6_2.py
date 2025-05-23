# print sum of Even numbers between 1 and 100. Use a loop to find and print the sum of all even numbers from 1 to 100.

def main():
    no=0
    for i in range(2,101,2):
        no=no+i
        print("Sum of Even number between 1 to 100 is : ",no)



if __name__=="__main__":
    main()