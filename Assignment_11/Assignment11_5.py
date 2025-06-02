# Write a recursive function to count how many zeros are in the given number.


def countZero(no,count=0):
    if no==0 and count > 0:
        return count
    if no%10==0:
        count=count+1
    return countZero(no//10,count)
    
    
def main():
    ret = countZero(100403454602014)
    print("There are : ",ret , "zeros")


if __name__=="__main__":
    main()