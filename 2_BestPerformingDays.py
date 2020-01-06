import pandas as pd

# read csv
df = pd.read_csv('all_stocks_5yr.csv')

for year in range(2013, 2018):
    yearstr = str(year)

    # Extract data by year
    dfyear = df[df['date'].str.startswith(yearstr)].copy()

    # Calculate daily return
    dfyear['return'] = (dfyear['close'] - dfyear['open']) / dfyear['open'] * 100

    # Calculate average of daily return across stocks
    dfyear = dfyear.groupby('date').mean().reset_index()
    dfyear = dfyear[['date', 'return']]

    # Print top 5 days with heighest return
    print(dfyear.sort_values('return', ascending=False)[:5][['date', 'return']])
