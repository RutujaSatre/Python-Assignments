# Plot a histogram of math marks.

import pandas as pd
import matplotlib.pyplot as plt

def Histogram():
    data = { 'Name': ['Amit','Sagar','Pooja'],'Math': [85,90,78],'Science' : [92,88,80],'English' : [75,85,82],'Total' : [252,263,240],'Status': ['Pass','Pass','Fail']}
    df = pd.DataFrame(data)
    plt.hist(df['Math'],bins = 20,color = 'lightgreen', edgecolor = 'darkgreen')
    plt.title("Distribution of Maths marks")
    plt.xlabel("Math Marks")
    plt.ylabel("Students")
    plt.grid(True)
    plt.show()

def main():
    Histogram()


if __name__ == "__main__":
    main()   