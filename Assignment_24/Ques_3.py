# Group students by gender and calculate average marks.


import pandas as pd

def average():
    data = { 'Name': ['Amit','Sagar','Pooja'],'Math': [85,90,78],'Science' : [92,88,80],'English' : [75,85,82], 'Gender' : ['Male', 'Male', 'Female']}
    df = pd.DataFrame(data)
    df = df.groupby('Gender')[['Math','Science','English']].mean()
    print(df)

def main():
    average()

if __name__=="__main__":
    main()