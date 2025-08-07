# Write a program which accept file name from user and create new file named as Demo.txt and copy all contents from existing file into new file.Accept file name through command line arguments.


import sys

def main():
    
    File = sys.argv[1]

    Source_file= open(File,'r')
    content = Source_file.read()
    Source_file.close()

    Destination_file = open('Demo.txt','w')
    Destination_file.write(content)
    Destination_file.close()
    
    print("Data Copied Successfully")

if __name__=="__main__":
    main()