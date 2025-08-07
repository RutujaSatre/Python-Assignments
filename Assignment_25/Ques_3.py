# Apply label Encoding to a 'City' column.
# data = {'City': ['Pune','Mumbai','Delhi','Pune','Delhi']}


import pandas as pd
from sklearn.preprocessing import LabelEncoder

def Encoding():
    data = {'City': ['Pune','Mumbai','Delhi','Pune','Delhi']}
    df = pd.DataFrame(data)
    label = LabelEncoder()

    df['City_Encode'] = label.fit_transform(df['City'])
    print(df)

def main():
    Encoding()

if __name__=="__main__":
    main()