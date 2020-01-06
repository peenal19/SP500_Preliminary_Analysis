import pandas as pd
import numpy as np

# read csv
df = pd.read_csv('all_stocks_5yr.csv')

# Filtering whole data frame for 2017 year data
df2017 = df[df['date'].str.startswith('2017', na=False)]

# Group by Stock Names
byName = df2017.groupby('Name')

# Calculate average closing price of each stock
meanPrice = byName.mean()['close']

# Merge result of average closing price with the actual data
mergedMean = pd.merge(df2017, meanPrice, how='inner', on=['Name'])

# calculate variance by (Price(daily) - Price(Mean))^2
mergedMean['variance'] = (mergedMean['close_x'] - mergedMean['close_y']) ** 2

# Extract Name and variance value
mergedMean = mergedMean[['Name', 'variance']]

# Calculate volatility by SQRT(Sum(variance)/n)
volatility = mergedMean.groupby('Name').mean()
volatility['volatility'] = np.sqrt(volatility['variance'])

# Extract top 10 volatile stocks
print(volatility.sort_values('volatility', ascending=False)[:10]['volatility'])
