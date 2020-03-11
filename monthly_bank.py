import pandas as pd
import csv
import os
import shutil



statement = pd.read_csv('A:\Jonathan\Downloads\history.csv', engine='python')
statement.drop(['Confirmation', 'Check Number'], axis=1, inplace=True,)
statement.drop(['Transfer Deposit','Cash Withdrawal'], ,inplace=True])


print (statement.head())