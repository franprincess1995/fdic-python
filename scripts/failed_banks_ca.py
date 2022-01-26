"""
This script should download the list of FDIC failed
banks and generate a new file containing
just the CA banks. It should also print out
the number of failed banks in CA.

See the TODO notes below for detailed requirements
on each step of the code.

USAGE:

    python failed_banks_ca.py

"""
# TODO: IMPORT MODULES HERE
import requests 
from datetime import datetime as dt
import csv

# URL TO THE FDIC BANKS DATA
url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/banklist.csv'

# TODO: Use the requests library to fetch the FDIC data
fdic_data = requests.get('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/banklist.csv')

# TODO: Use the "with" statement and "open" function,
# (you don't need to use CSV for this step) to write the file contents
# (as returned by requests) to a local file caled "banklist.csv"
with open('banklist.csv', 'w') as bank_data:
    bank_data.write(fdic_data.text)

# ONce you leave with the with block (i.e. have unindented)
# the bank_data file handle has been automatically closed and 
# is no longer available for write or other file operations
# TODO: Use "with" and "open" along with the CSV module
# to read the local "banklist.csv"
CA_banks =[]

with open('banklist.csv', 'r') as banklist:
    csv_reader = csv.reader(banklist)
    columns = next(csv_reader)
    CA_banks.append(columns)
    for row in csv_reader:
        if row[2]=='CA':
            dt_object_1 = dt.strptime(row[-2], "%d-%b-%y").strftime("%Y-%m-%d")
            row[-2] = dt_object_1
            CA_banks.append(row)

with open ('failed_banks_ca.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    for row in CA_banks:
        writer.writerow(row)

print(f'There are {(len(CA_banks)-1)} failed banks in CA.')

#header?
#datetime

## for row in banklist:
     ##   columns = row.split(',')
      ##  if columns[2] == 'CA':
       ##     CA_banks.append(row.strip('\n'))
            

    # TODO: Perform the following actions on each row of "banklist.csv"
    # - filter the data for just California banks
    # - reformat the Closing Date value in each row to YYYY-MM-DD format
    #   using the datetime module's strptime and strftime functions
    # - Save the updated data (so you can create a new file below)


# TODO: Use the "with" statement and "open" function,
# along with the CSV module, to write a new file called "failed_banks_ca.csv"
# The new file must contain the same header row and columns as the original file!


# TODO: print the sentence "There are X failed banks in CA.",
# replacing the X dynamically with a count of the CA banks.
