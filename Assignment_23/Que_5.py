# Replace "Pooja" with "Puja" in the  "Name" column.

import pandas as pd

def Replace():
    data = { 'Name': ['Amit','Sagar','Pooja'],'Math': [85,90,78],'Science' : [92,88,80],'English' : [75,85,82]}
    df = pd.DataFrame(data)
    df = df.replace({'Pooja':'Puja'})
    print(df)

def main():
    Replace()
if __name__=="__main__":
    main()