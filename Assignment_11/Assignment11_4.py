# Write a recursion function to calculate x^n.

def Power(no1,no2):
    no=no1**no2
    return no

def main():
    ret = Power(2,3)
    print("Power is : " ,ret)


if __name__=="__main__":
    main()

