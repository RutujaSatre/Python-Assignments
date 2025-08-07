# Create a bar plot of student names vs total marks.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def BarPlot():
    data = { 'Name': ['Amit','Sagar','Pooja'],'Math': [85,90,78],'Science' : [92,88,80],'English' : [75,85,82]}
    df = pd.DataFrame(data)
    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)

    sns.barplot(x = "Name",y = "Total",color = '#00BCAD', data = df)
    plt.xlabel("Students Name")
    plt.ylabel("Total Marks")
    plt.title("Marks Graph")
    plt.show()

def main():
    BarPlot()

if __name__=="__main__":
    main()