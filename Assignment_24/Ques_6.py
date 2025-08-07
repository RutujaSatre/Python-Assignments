# Count how many students passed.

import pandas as pd

def Students():
    data = { 'Name': ['Amit','Sagar','Pooja'],'Math': [85,90,78],'Science' : [92,88,80],'English' : [75,85,82],'Total' : [252,263,240],'Status': ['Pass','Pass','Fail']}
    df = pd.DataFrame(data)
    df = df[df['Status'] == 'Pass'].shape[0]
    print(df)


def main():
    Students()

if __name__=="__main__":
    main()