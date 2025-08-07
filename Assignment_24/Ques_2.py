# Create a gender column and perform one-hot encoding.

import pandas as pd

def Encoding():
    data = { 'Name': ['Amit','Sagar','Pooja'],'Math': [85,90,78],'Science' : [92,88,80],'English' : [75,85,82]}
    df = pd.DataFrame(data)
    df['Gender'] = ['Male','Male','Female']
    df = pd.get_dummies(df,columns=['Gender'])
    print(df)

def main():
    Encoding()

if __name__=="__main__":
    main()