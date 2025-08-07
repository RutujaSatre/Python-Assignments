# Rename 'Math'columns with 'Mathematics.

import pandas as pd

def Rename():
    data = { 'Name': ['Amit','Sagar','Pooja'],'Math': [85,90,78],'Science' : [92,88,80],'English' : [75,85,82],'Total' : [252,263,240],'Status': ['Pass','Pass','Fail']}
    df = pd.DataFrame(data)
    df = df.rename(columns={'Math':'Mathematics'})
    print(df)

def main():
    Rename()

if __name__=="__main__":
    main()
