import requests
from datetime import datetime as dt
import csv

url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/banklist.csv"

fdic_data = requests.get(
    "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/banklist.csv"
)

with open("banklist.csv", "w") as bank_data:
    bank_data.write(fdic_data.text)

CA_banks = []

with open("banklist.csv", "r") as banklist:
    csv_reader = csv.reader(banklist)
    columns = next(csv_reader)
    CA_banks.append(columns)
    for row in csv_reader:
        if row[2] == "CA":
            dt_object_1 = dt.strptime(row[-2], "%d-%b-%y").strftime("%Y-%m-%d")
            row[-2] = dt_object_1
            CA_banks.append(row)

with open("failed_banks_ca.csv", "w") as outfile:
    writer = csv.writer(outfile)
    for row in CA_banks:
        writer.writerow(row)

print(f"There are {(len(CA_banks)-1)} failed banks in CA.")
