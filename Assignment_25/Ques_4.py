# Apply One-Hot Encoding to a 'Department' column.
# data = {'Department': ['HR','IT','Finance','HR','IT']}

import pandas as pd

def encode():
    data = {'Department': ['HR','IT','Finance','HR','IT']}
    df = pd.DataFrame(data)
    df = pd.get_dummies(df,columns=['Department'])
    print(df)

def main():
    encode()

if __name__=="__main__":
    main()
