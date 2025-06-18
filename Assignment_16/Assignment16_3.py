# Write a python script to count the number of lines, words , and characters in a given file.

def main():
    file = open('student.txt','r')
    lines = file.readlines()

    num_lines = len(lines)  
    num_words =sum(len(line.split())for line in lines)
    num_chars = sum(len(line) for line in lines)

    print("Total lines : ",num_lines)
    print("Total words : ",num_words)
    print("Total characters : ",num_chars)

if __name__=="__main__":
    main()