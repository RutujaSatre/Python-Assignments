# Write a program which accept file name from user and open that file and display the contents of that file on screen.


def ChkContent(file):
    file = open(file,'r')
    content = file.read()
    print(content)

def main():
    print("File name : ")
    fname = input()
    ChkContent(fname)

if __name__=="__main__":
    main()
