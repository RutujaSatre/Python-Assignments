# Write a python program to copy the contents of one file into another file.

def main():
    sourcefile = open('student.txt','r')
    destinationfile = open('Demo.txt','w')

    for line in sourcefile:
        destinationfile.write(line)
       
if __name__=="__main__":
    main()