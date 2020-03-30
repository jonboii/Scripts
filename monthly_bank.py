import pandas as pd


df = pd.read_csv('A:\Jonathan\Downloads\history.csv', engine='python')
df.drop(['Confirmation', 'Check Number', 'Unnamed: 5'], axis=1, inplace=True)

#Removing unwanted strings in description
df['Description'] = df['Description'].str.replace('Transfer Deposit VIRTUAL BRANCH TRANSFER FROM', "").str.replace('Cash Withdrawal', "").str.replace('POS', "").str.replace('XXXXXX', "").str.replace('\d+', "").str.replace('WHITE RIV JCTVT', "").str.replace(' ', "").str.replace(r'\W', "").str.replace('MN', "").str.replace('NY', "")

print (df.head())