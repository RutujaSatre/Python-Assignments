# Accept number from user and print its multiplication table up to 10.

def main():
    print("Enter a number : ")
    no=int(input())

    print("Table : " )

    for i in range(1,11):
        
        val = no*i
       
        print(no,"*",i,"=",val)

if __name__=="__main__":
    main()