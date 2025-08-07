# Write a program which accept two file names from user and compare contents of both the files. If both the files contains same contents then display success otherwise display failure. Accept names of both the files from command line.

import sys

def main():
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]

    f1 = open(filename1,'r')
    f2 = open(filename2,'r')

    if (f1.read() == f2.read()):
        print("success")
    else:
        print("Failure")

if __name__=="__main__":
    main()
