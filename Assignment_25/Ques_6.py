# Replace multiple values in a column using a dictionary.
# data = {'Grade': ['A+','B','A','C','B+']}
# Replace as 
# 'A+' : 'Excellent'
# 'A' : 'very good'
# 'B+' : 'Good'
# 'B' : 'Average'
# 'C' : 'Poor'

import pandas as pd
def RepalceValue():
    data = {'Grade': ['A+','B','A','C','B+']}
    df = pd.DataFrame(data)
    Replace = {'A+' : 'Excellent','A' : 'very good','B+' : 'Good','B' : 'Average','C' : 'Poor'}
    df['Grade'] = df.replace(Replace)
    print(df)


def main():
    RepalceValue()

if __name__=="__main__":
    main()
