# Replace values in 'Marks' less than 50 with 'Fail' using where().
# data = {'Marks' : [45,67,88,32,76]}


import pandas as pd
import numpy as np

def replace():
    data = {'Marks' : [45,67,88,32,76]}
    df = pd.DataFrame(data)
    df['Marks'] = np.where(df['Marks']<50,'Fail',df['Marks'])
    print(df)

def main():
    replace()

if __name__=="__main__":
    main()