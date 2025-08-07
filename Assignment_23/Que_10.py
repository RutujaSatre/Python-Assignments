# Drop the 'English' column from original DataFrame.


import pandas as pd

def DropTable():
    data = { 'Name': ['Amit','Sagar','Pooja'],'Math': [85,90,78],'Science' : [92,88,80],'English' : [75,85,82]}
    df = pd.DataFrame(data)
    df = df.drop(columns = 'English')
    print(df)


def main():
    DropTable()

if __name__=="__main__":
    main()