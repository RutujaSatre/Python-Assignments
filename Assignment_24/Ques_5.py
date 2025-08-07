# Add a new column  'Status' where students with total>= 250 are 'Pass', else 'Fail'.


import pandas as pd

def Status():
    data = { 'Name': ['Amit','Sagar','Pooja'],'Math': [85,90,78],'Science' : [92,88,80],'English' : [75,85,82]}
    df = pd.DataFrame(data)
    df['Total'] = df[['Math','Science','English']].sum(axis = 1)
    df['Status'] = df['Total'].apply(lambda x: 'Pass' if x>=250 else 'Fail')
    print(df)

def main():
    Status()

if __name__=="__main__":
    main()