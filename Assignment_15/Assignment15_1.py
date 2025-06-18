# Write a program which accepts file name from user and check whether that file exists in current directory or not.


import os 

def ChkFileExist(DirectoryName):
    flag = os.path.exists(DirectoryName)
    
    if(flag==False):
        print("File does not exist.. ")

    else:
        print("File exists..")

def main():
    ChkFileExist(input("Enter file name :"))

if __name__=="__main__":
    main()