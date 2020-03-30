
#Trying to edit the bad csv to get rid of "" in the final column
with opetn('history.csv', 'W') as file:
    writer = csv.writer(file)
    writer.
changes = [
    ['""','",']
]


#to rename file and put it in a better location after it's done being edited
os.rename("A:\Jonathan\Downloads\history.csv", "A:\Jonathan\Downloads\NEWNAME_PROBABLY_DATE_RANGE-TAKEN_FROM_CSV.csv")
shutil.move("A:\Jonathan\Downloads\NEWNAME_PROBABLY_DATE_RANGE-TAKEN_FROM_CSV.csv", "A:\Jonathan\Documents\Money\Statements\NEWNAME_PROBABLY_DATE_RANGE-TAKEN_FROM_CSV.csv")
file = "A:\Jonathan\Documents\Money\Statements\NEWNAME_PROBABLY_DATE_RANGE-TAKEN_FROM_CSV.csv")

df['Description'] = df['Description'].str.replace('Transfer.+', "").str.replace('Cash Withdrawal', "").str.replace('POS', "").str.replace('XX.+', "").str.replace('\d+', "").str.replace('WHITE RIV JCTVT', "").str.replace(' ', "").str.replace(r'\W', "").str.replace('MN', "").str.replace('NY', "").str.replace('NORTHFIELDVT', "").str.replace('RANDOLPHVT', "").str.replace('KY', "")





replacements = {
    'Description': {
        replace'(Transfer.+)': "",
        replace'(Cash.+)': "",
        replace'(POS)': "",
        replace'(XX.+)': "",
        r'(\d+)': "",
        r'(WHITE RIV.+)': "",
        r'(/)': "",
        r'(:)': "",
        r'( )': "",
        r'(MN)': "",
        r(r'\W'): "",
        r'(NY)': "",
        r'(NORTHFI.+)': "",
        r'(RANDOLPHVT)': "",
        r'(KY)': "",
    }
}
df.replace(replacements, regex=True, inplace=True)