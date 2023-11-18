import csv
import sqlite3
import random 
from db import * 

# org_list = get_column("organisation")
# records_list = get_column("records lost")
# dates_list = get_column("date")
# sector_list = get_column("sector")
# sens_list = get_column("data sensitivity")

def model_specified(colArr):
    dataDict = {}
    i = 0
    with open('data_breaches.csv') as f:
        r = csv.DictReader(f)
        for row in r:
            if (i < 10):
                # setting empty array of row elements so we can add specific cols
                rowElements = []
                orgName = row["organisation"]
                if (orgName not in dataDict):
                    # only if not already in table and over certain range for records lost
                    # new entry into dictionary
                    dataDict[orgName] = []
                for colName in colArr:
                    rowElements.append(row[colName])
                dataDict[orgName].append(rowElements)
            i+=1
        return dataDict

print(model_specified(["records lost", "date"]))

                    