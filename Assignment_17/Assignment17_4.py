# Accept 10 numbers from the user and write them into a file named numbers.txt, each on a new line.


def main():
    fobj = open("number.txt",'w') 
    for i in range(10):
        number = input("Enter number :")
        fobj.write(number+"\n")   
    
    print("Numbers saved successfully")

if __name__=="__main__":
    main()