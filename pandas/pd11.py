"""
11. Given is a dataframe showing Company Names (cname) and corresponding Profits 
(profit). Convert the values of Profit column such that values in it greater than 0 are 
set to True and the rest are set to False.


"""


# import pandas as pd
#
# details = {
#     'cname' : ['a','b','c','d'],
#     'profit' : [24,25,0,-27],
# }
#
# df = pd.DataFrame(details)
#
# df.loc[df.profit <= 0,'profit'] = False
# df.loc[df.profit > 0,'profit'] = True
# print(df)

#df['profit'] = df['profit'].apply(lambda x:x>0)
#print(df)

import pandas as pd

# Sample DataFrame
data = {
    'cname': ['Company A', 'Company B', 'Company C', 'Company D'],
    'profit': [10000, -5000, 0, 25000]
}

df = pd.DataFrame(data)

# Convert Profit column to True/False based on the condition
df['profit'] = df['profit'] > 0
print(df)
