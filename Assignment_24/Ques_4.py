# plot a pie chart of subject marks for 'Sagar'.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def PieChart():
    data = { 'Name': ['Amit','Sagar','Pooja'],'Math': [85,90,78],'Science' : [92,88,80],'English' : [75,85,82]}
    df = pd.DataFrame(data)
    df = df[df['Name']=='Sagar'][['Math','Science','English']].iloc[0]
    plt.pie(df,labels = df.index, autopct='%1.1f%%')
    plt.title("Sagars Marks Distribution")
    plt.show()

def main():
    PieChart()

if __name__=="__main__":
    main()