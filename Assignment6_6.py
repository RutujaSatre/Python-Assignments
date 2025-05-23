# Print Triangle pattern using Nested Loop.

def main():
    num=5

    for i in range(1,num+1):
        for j in range(i):
            print("*",end=" ")
        print()
        


if __name__=="__main__":
    main()