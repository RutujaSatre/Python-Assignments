# Use the datafeame from Q.1 and print descriptive statistics using .describe()

import pandas as pd

def Descriptive():
    data = { 'Name': ['Amit','Sagar','Pooja'],'Math': [85,90,78],'Science' : [92,88,80],'English' : [75,85,82]}
    df = pd.DataFrame(data)
    print("Statistical Summary is : \n\n",df.describe())


def main():
    Descriptive()

if __name__=="__main__":
    main()