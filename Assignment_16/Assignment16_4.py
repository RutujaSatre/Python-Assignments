# Accept 10 numbers from user and write them into a file named number.txt,each of a new line.

def main():
    
    fopen = open('number.txt','w')

    print("Enter 10 Numbers : ")
    
    for i in range(10,21):
        value = input(i+1)

        fopen.write(value+'\n')

    print("----------------------")

if __name__=="__main__":
    main()