# This file is not part of the Flask application
# This file was only created to import the data from "tabledata.csv" into the "filenaming.db" SQL file
# This file will create duplicate entries if it is run again

import csv

from cs50 import SQL

db = SQL("sqlite:///filenaming.db")

# Open the CSV file
with open('tabledata.csv', 'r', newline='') as csvfile:
    tablesites = csv.reader(csvfile)
    print(tablesites)

    data = []
    # Only name and masterid have so far been located.
    # If a better data source is located in the future, edit below to include additional rows for "permit" or "county"
    for row in tablesites:
        dict = {'name':row[0], "masterid":row[2]}
        data.append(dict)
        print(dict['name'])
        print(dict['masterid'])
        # The next line is currently commented in order to prevent the file from inadvertently adding SQL entries
        #db.execute("INSERT INTO facilities (name, masterid) VALUES (?, ?)", dict['name'], dict['masterid'])
