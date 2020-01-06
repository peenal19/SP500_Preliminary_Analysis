import pandas as pd

# read csv
df = pd.read_csv('all_stocks_5yr.csv')

# 1. Filtering whole data frame for 2017 year data
df2017 = df[df['date'].str.startswith('2017', na=False)]

# 2.
# Group by Stock Names
byName = df2017.groupby('Name')

# Get Maximum and Minimum Dates
maxDate = byName.max()['date'].reset_index()
minDate = byName.min()['date'].reset_index()

# Join the maximum and minimum dates with the actual data
maxdf2017 = pd.merge(df2017, maxDate, how='inner', on=['Name', 'date'])
mindf2017 = pd.merge(df2017, minDate, how='inner', on=['Name', 'date'])

# Extract closing price of the last day of 2017
maxdf2017 = maxdf2017[['Name', 'close']]

# Extract opening price of the first day of 2017
mindf2017 = mindf2017[['Name', 'open']]

# Merge both closing and opening price of the year in same dataframe
merged2017 = pd.merge(maxdf2017, mindf2017, how='inner', on='Name')

# Calculate % return for the whole year
merged2017['return'] = (merged2017['close'] - merged2017['open']) / merged2017['open'] * 100

# extract best and worst performing stocks of 2017
print('2017 Best performing Stocks')
print(merged2017.sort_values('return', ascending=False)[:5][['Name', 'return']])
print()
print()
print('2017 Worst performing Stocks')
print(merged2017.sort_values('return')[:5][['Name', 'return']])
