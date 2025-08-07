# Accept file name and one string from user and return the frequency of that string from file.


import sys

def main():
    filename = sys.argv[1]
    string = sys.argv[2]

    file = open(filename,'r')
    content = file.read()

    count = content.count(string)

    print("String : ",count)

if __name__=="__main__":
    main()