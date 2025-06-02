# Write a recursive function to calculate sum from 1 to N.

sum = 0

def Sum(no):
    global sum
    if(no>=1):
        sum=sum+no
        no = no-1
    
        Sum(no)
    return sum

def main():
    ret = Sum(5)
    print("Sum of numbers : ",ret)

if __name__=="__main__":
    main()