# Export the final DataFrame to a CSV file.

import pandas as pd

def main():
    data = { 'Name': ['Amit','Sagar','Pooja'],'Math': [85,90,78],'Science' : [92,88,80],'English' : [75,85,82],'Total' : [252,263,240],'Status': ['Pass','Pass','Fail']}
    df = pd.DataFrame(data)
    df.to_csv('Student_Result.csv',index = False)
    print(df)

if __name__=="__main__":
    main()