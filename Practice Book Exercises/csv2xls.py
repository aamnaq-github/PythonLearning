# Problem 70: Write a program csv2xls.py that reads a csv file and exports it as Excel file. The prigram should
# take two arguments. The name of the csv file to read as first argument and the name of the Excel file to write as
# the second argument.
def csv2xls(csv_file, excel_file):
    source = open(csv_file, 'r').read()
    print('\nExporting', excel_file)
    destination = open(excel_file, 'w')
    destination.write(source)
    destination.close()