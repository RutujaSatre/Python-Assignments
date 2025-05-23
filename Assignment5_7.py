# Accept the length and width of a rectangle. Calculateand display the area and perimeter.

def main():
    print("Enter length : ")
    num1 = int(input())

    print("Enter width : ")
    num2 = int(input())

    area = num1 * num2
    peri = 2*(num1 + num2)

    print("Area of Rectangle is :",area)
    print("Perimeter of Rectangle is :",peri)


if __name__=="__main__":
    main()