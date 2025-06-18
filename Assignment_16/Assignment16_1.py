# Write a python program to create a text file named student.txt and write the names of 5 students into it.

def main():
    fopen = open("student.txt","w")
    fopen.write("Students name are : \n")
    fopen.write("Rutuja\n")
    fopen.write("Purva\n")
    fopen.write("Pranita\n")
    fopen.write("Ramesh\n")
    fopen.write("Sumitra\n")



if __name__=="__main__":
    main()