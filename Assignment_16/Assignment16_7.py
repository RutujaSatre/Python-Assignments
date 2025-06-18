# Create a file marks.txt with student name and marks. Then read the file and display students who scored more than 75.

def main():
    file = open('marks.txt','w')
    file.write("Mayra 98\n")
    file.write("Ram 74\n")
    file.write("Sidhi 82\n")
    file.write("Surbhi 78\n")
    file.write("Sandhya 70\n")

    file = open('marks.txt','r')
    print("Students who scored more than 75 marks : ")
    for i in file:
        name,marks = i.strip().split()
        if int(marks)>75:
            print(name)
            print(marks)

if __name__=="__main__":
    main()