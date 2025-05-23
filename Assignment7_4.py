# Accept a list of numbers and use reduce() (from functools) to find the product of all numbers. 

from functools import reduce

fProduct = lambda x,y: x*y

def main():
 print("Enter list : ")
 no = list(map(int,input().split()))
 
 RData = reduce(fProduct,no)
 print("Filter Output: ",RData)

if __name__=="__main__":
  main()