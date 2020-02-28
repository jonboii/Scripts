import pandas as pd

statement = pd.read_csv('/home/prism/Desktop/history.csv', engine='python')

statement.drop(['Confirmation', 'Check Number'], axis=1, inplace=True)

print (statement.head())