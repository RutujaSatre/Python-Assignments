# Accept a single character from the user  and check if it is a vowel (a,e,i,o,u). If not , print its a consonant.

def main():
    print("Enter a Character : ")
    val=input()

    if val in ("a" , "e ", "i ", "o ", "u"):
        print(val,"is a vowel")
    else:
        print(val,"is a consonant")


if __name__=="__main__":
    main()