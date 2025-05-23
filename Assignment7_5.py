# Write a function that accepts a string and checks whether it is a palindrome.
ChkPalindrome = lambda no : no==no[::-1]
def main():
    print("Enter a String : ")
    value = input()

    print(ChkPalindrome(value),"Palindrome")

if __name__=="__main__":
    main()