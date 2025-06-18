# Write a program to read a file line by line and display only those lines that contain more than 5 words.

def main():
    file = open('student.txt','r') 
    for num_line,line in enumerate(file,1):
        words = line.strip().split()
        if len(words)>5:
            print(line)
            print(num_line)

    file.close()
    
if __name__=="__main__":
    main()