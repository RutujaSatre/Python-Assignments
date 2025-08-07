# Create a DataFrame with missing values and fill them with column mean.
# data2 = { 'Name': ['Amit','Sagar','Pooja'],
#          'Math': [np.nan,76,88],
#          'Science' : [91,np.nan,85]}

import pandas as pd
import numpy as np

def MeanValues():
    data2 = { 'Name': ['Amit','Sagar','Pooja'],'Math': [np.nan,76,88],'Science' : [91,np.nan,85]}
    df = pd.DataFrame(data2) 
    df[['Math','Science']] = df[['Math','Science']].fillna(df[['Math','Science']].mean())
    print(df)
   


def main():
    MeanValues()

if __name__=="__main__":
    main()