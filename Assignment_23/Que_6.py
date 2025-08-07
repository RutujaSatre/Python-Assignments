# Sort the Dataframe by 'Total' marks in decending order.

import pandas as pd

def DescendingOrder():
    data = { 'Name': ['Amit','Sagar','Pooja'],'Math': [85,90,78],'Science' : [92,88,80],'English' : [75,85,82]}
    df = pd.DataFrame(data)
    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
    df = df.sort_values(by = 'Total', ascending=False)
    print(df)


def main():
    DescendingOrder()

if __name__=="__main__":
    main()