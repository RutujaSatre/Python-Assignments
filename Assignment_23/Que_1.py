# Create a DataFrame for student marks and print basic information like shape, columns, and data types.
# data = { 'Name': ['Amit','Sagar','Pooja'],
#          'Math': [85,90,78],
#          'Science' : [92,88,80],
#          'English' : [75,85,82]}


import pandas as pd

def StudentMarks():
    data = { 'Name': ['Amit','Sagar','Pooja'],'Math': [85,90,78],'Science' : [92,88,80],'English' : [75,85,82]}
    df = pd.DataFrame(data)
    print(df.shape)
    print(df.columns)
    print(type(data))


def main():
    StudentMarks()

if __name__=="__main__":
    main()