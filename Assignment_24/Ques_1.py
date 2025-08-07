# Normalize the 'Math' scores using Min-Max scaling.

import pandas as pd

def Scaling():
    data = { 'Name': ['Amit','Sagar','Pooja'],'Math': [85,90,78],'Science' : [92,88,80],'English' : [75,85,82]}
    df = pd.DataFrame(data)
    min = df['Math'].min()
    max = df['Math'].max()

    df['Math_Normalise'] = (df['Math'] - min) / (max - min)
    print(df)

def main():
    Scaling()

if __name__=="__main__":
    main()