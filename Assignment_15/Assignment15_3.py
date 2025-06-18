# Write a program which accept file name from user and create new file named as Demo.txt and copy all contents from existing file into new file. Accept file name through command line arguments.

import sys

def main():
    file1 = open('Demo.txt','r')
    file2 = sys.argv[1]
    fopen = open(file2,'a')

    fopen.writelines(file1)
    

if __name__=="__main__":
    main()