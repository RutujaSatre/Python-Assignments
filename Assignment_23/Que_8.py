# Plot a line chart of marks for 'Amit' across all subjects.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def LineChart():
    data = { 'Name': ['Amit','Sagar','Pooja'],'Math': [85,90,78],'Science' : [92,88,80],'English' : [75,85,82]}
    df = pd.DataFrame(data)
    df = df[df['Name']=='Amit'].iloc[0,1:]
    sns.lineplot(data=df,color = 'red' , linewidth=2)
    plt.xlabel("Subject Names")
    plt.ylabel("Marks")
    plt.title("Amit's Marks")

    plt.show()

def main():
    LineChart()

if __name__=='__main__':
    main()