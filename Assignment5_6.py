# Accept temperature in Celsius and convert it to Fahrenheit using the formula: F = (C * 9/5 + 32)

def  main():
    print("Enter temperature in Celsius ")
    C = int(input())

    F = (C * 9/5 + 32)
    print("Temperature in Fahrenheit : ",F,"F")

if __name__=="__main__":
    main()