# Create a DataFrame with 'Age' and 'Purchased' columns and split into train/test sets.
# data = {'Age' : [22,25,47,52,46,56], 'Purchased': [0,1,1,0,1,0]}

import pandas as pd
from sklearn.model_selection import train_test_split

def dataframe():
    data = {'Age' : [22,25,47,52,46,56], 'Purchased': [0,1,1,0,1,0]}
    df = pd.DataFrame(data)

    x = df['Age']
    y = df['Purchased']

    x_train, x_test, Y_train, Y_test = train_test_split(x,y, test_size=0.2,random_state=42)

    print("X_train is :\n", x_train)
    print("X_test is :\n", x_test)
    print("Y_train is :\n", Y_train)
    print("Y_test is :\n", Y_test)


def main():
    dataframe()

if __name__=="__main__":
    main()