# Write a program which accept file name from user and open that file and display the contents of that file on screen.

import os 

def main():
    print("Enter the name of a file that you want to read : ")
    FileName = input()

    ret = os.path.exists(FileName)

    if(ret==True):
        print("File is present in current directory")
        fobj=open(FileName,"r")
        data=fobj.read()

        print("Data from file is : ",data)

        fobj.close()
        
    else:
        print("There is no such file")
  

if __name__=="__main__":
    main()