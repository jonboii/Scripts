
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