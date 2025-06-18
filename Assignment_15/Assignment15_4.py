# Write a program which accept two file names from user and compare contents of both the files. If both the files contains same contents then display success otherwise display failure .Accept names of both the files from command line.

import sys

def main():
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    f1 = open(file1,'r')
    f2 = open(file2,'r')

    if (f1.read() == f2.read()):
        print("success")
    else:
        print("Failure")

if __name__=="__main__":
    main()