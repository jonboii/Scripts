import pandas as pd
import csv
import os
import shutil



statement = pd.read_excel('A:\Jonathan\Downloads\history.xls', engine='python')
statement.drop(['Confirmation', 'Check Number', 'Unnamed: 5'], axis=1, inplace=True)

print (statement.head())