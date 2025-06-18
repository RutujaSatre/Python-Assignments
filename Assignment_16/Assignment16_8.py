# Write a script to remove all blank lines from a file. Save the cleaned output to new file.

def main():
    file1 =  open('student.txt', 'r')
    file2 = open('output.txt', 'w') 
    for line in file1:
        if line.strip():
            file2.write(line)


if __name__=="__main__":
    main()