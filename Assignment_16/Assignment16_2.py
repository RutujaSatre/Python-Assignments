# Write a program to read and display the contents of a file data.txt

def main():
    
    fread = open('data.txt','r')
    file = fread.read()
    print(file)
if __name__=="__main__":
    main()