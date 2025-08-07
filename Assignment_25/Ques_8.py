# Fill missing values in a numeric column using interpolation.
# data = {'Marks': [85,np.nan,90,np.nan,95]}


import pandas as pd
import numpy as np

def Interpolation():
    data = {'Marks': [85,np.nan,90,np.nan,95]}
    df = pd.DataFrame(data)
    i_df = df.interpolate()
    print(i_df)

def main():
    Interpolation()


if __name__=="__main__":
    main()