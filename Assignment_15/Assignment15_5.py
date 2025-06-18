# Accept file name and one string from user and return the frequency of that string from file.

def main():
    
    file_name = input("Enter File name : ")
    stri = print(input("Enter String"))
    count = 0 
    file = open(file_name,'r')

    content = file.read()
    words = content.split()
    count += words.count(stri)

    print("Frequency is : ",count)
    

if __name__=="__main__":
    main()