# Detect outliers in the 'Salary' column using the IQR method.
# data = {'Salary': [25000,27000,29000,31000,50000,100000]}


import pandas as pd

def IQR():
    data = {'Salary': [25000,27000,29000,31000,50000,100000]}
    df = pd.DataFrame(data)    
    Q1 = df['Salary'].quantile(0.25)
    Q3 = df['Salary'].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df['Salary'] < lower_bound) | (df['Salary']> upper_bound)]
    print("Outliers detect using IQR method : ")
    print(outliers)

def main():
    IQR()

if __name__=="__main__":
        main()