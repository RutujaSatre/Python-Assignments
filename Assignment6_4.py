# Accept a number and print its factorial using a for loop.

def main():
    print("Enter a number : ")
    num = int(input())
    
    Fact = 1
    for i in range(1 , num+1):
        Fact = Fact * i

    print("Factorial of",num,"is",Fact)
    

if __name__=="__main__":
    main()