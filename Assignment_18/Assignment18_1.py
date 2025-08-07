# Write a program which accepts file name from user and check whether that file exists in current directory or not.

import os
def CheckDirectory(Dirname):
    flag = os.path.exists(Dirname)

    if(flag==False):
        print("File is not exist in current directory")
        exit()
    else:
        print("File exist in current directory")

def main():
    print("Enter your File name : ")
    Dirname = input()
    CheckDirectory(Dirname)


if __name__=="__main__":
    main()