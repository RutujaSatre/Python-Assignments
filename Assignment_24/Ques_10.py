# Plot a boxplot for English marks to check distribution and outliers.

import pandas as pd
import matplotlib.pyplot as plt

def Boxplot():
    data = { 'Name': ['Amit','Sagar','Pooja'],'Math': [85,90,78],'Science' : [92,88,80],'English' : [75,85,82],'Total' : [252,263,240],'Status': ['Pass','Pass','Fail']}
    df = pd.DataFrame(data)
    plt.boxplot(df["English"],vert = False, patch_artist=True,
            boxprops=dict(facecolor='lightgreen'),
            medianprops=dict(color='red'),
            flierprops=dict(marker='o', markerfacecolor='blue'))
    plt.title("Boxplot for English Marks")
    plt.xlabel("English Marks")
    plt.grid(True)
    plt.show()

def main():
    Boxplot()

if __name__=="__main__":
    main()