## Importing data by referencing https://medium.com/casual-inference/the-most-time-efficient-ways-to-import-csv-data-in-python-cc159b44063d
## Using docs from https://docs.python.org/3/library/stdtypes.html#dict
## Also using docs:  https://docs.python.org/3/library/csv.html per medium article suggestion
import csv

def classifyByConditions(filename='Trails.csv'):
    with open(filename) as fn:
        global inputDict
        inputDict = csv.DictReader(fn)
        conditionsDict = dict()
        for dictItem in inputDict:
            conditionStr = dictItem['CONDITION']
            trailStr = dictItem['TRAIL_NAME']
            if dictItem['CONDITION'] not in conditionsDict:
                conditionsDict[conditionStr] = []
            else:
                conditionsDict[conditionStr].append(trailStr)
        for dictItem in conditionsDict:
            print("Trails in ", dictItem,"Condition: \n")
            print(conditionsDict[dictItem])
classifyByConditions()