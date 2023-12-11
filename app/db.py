import csv
import sqlite3
import random 
import codecs

# org_list = get_column("organisation")
# records_list = get_column("records lost")
# dates_list = get_column("date")
# sector_list = get_column("sector")
# sens_list = get_column("data sensitivity")

def model_specified(colArr, recordMin, yearMin):
    dataDict = {}
    with open('data_breaches.csv', 'r', encoding='utf-8') as f:
        r = csv.DictReader(f)
        for row in r:
            if (row["date"]!=''):
                recordNum = int(row["records lost"].replace(",",""))
                yearNum = int(row["year   "])
                # only adding values with these conditions
                if (yearNum>=yearMin and recordNum>=recordMin):
                    # setting empty array of row elements so we can add specific cols
                    rowElements = []
                    orgName = row["organisation"]
                    if (orgName not in dataDict):
                        # only if not already in table and over certain range for records lost
                        # new entry into dictionary
                        dataDict[orgName] = []
                    for colName in colArr:
                        dataDict[orgName].append(row[colName])
        return dataDict

def createArray(dataDict):
    orgArr = []
    yearArr = []
    recordArr = []
    for row in dataDict:
        yearArr.append(int(dataDict[row][1]))
        recordArr.append(int(dataDict[row][0].replace(",","")))
        orgArr.append(row)
    return [recordArr, yearArr, orgArr]

def main(): 
    testData = model_specified(["records lost", "date", "year   "], 1000000)
    for org in testData:
        print(testData[org])



                    