import pandas as pd
import csv
import os
import shutil



statement = pd.read_csv('Path', engine='python')
statement.drop(['Confirmation', 'Check Number', 'Unnamed: 5'], axis=1, inplace=True)

#Trying to remove transsfer deposit and cash withdrawal
s = pd.Series()
s.str.lstrip([Transfer])

print (statement.head())
