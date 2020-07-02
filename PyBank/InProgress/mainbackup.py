
#Import modules
import os
import csv

#Zero total
total=0
changetotal=0

#Define file path
csvpath = os.path.join("..","Resources","budget_data.csv" )

#Read CSV file
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile)
    #Skip the header row 
    csvheader = next(csvreader)
    #Count number of lines in CSV file, and print info using f string
    lines = len(list(csvreader))
    print(f"There are {lines} months of data contained in the dataset.")
   
#ReadCSV files
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile)
    #Skip the header row 
    csvheader = next(csvreader)
    for row in csv.reader(csvfile):
        bestdate = str(row[0])
        worstdate = str(row[0])
        old = float(row[1])
        total = float(row[1]

        #print(f"OLD: {old}.")
        for row in csv.reader(csvfile)
            total = float(row[1])+total
            #print(f"RUNNING TOTAL: {total}.")
            new = float(row[1])
            #print(f"NEW: {new}.")
            change = old - new
            oldchange = change
            highdate = (row[0])
            #print(F"CHANGE: {change}.")
            old = new
            #print(f"OLD: {old}.")
            changetotal = changetotal + change
            #print(f"RUNNING CHANGE TOTAL: {changetotal}.")  
            newchange = change
            if newchange <= oldchange:
                highchange = oldchange
            else:
                highchange = newchange
                bestdate = (row[0])  
            #if currentlow <= current:
                #currentlow = current
                #lowdate = (row[0])
            #else:
                #currentlow = currentlow
                
        currencytotal = "${:,.2f}".format(total)
        currencychangetotal = "${:,.2f}".format(changetotal/(lines-1))     
        currencyhigh = "${:,.2f}".format(highchange)
        currencylow = "${:,.2f}".format(currentlow)
    print(f"The total profit/loss for all months and years in the dataset is: {currencytotal}.")
    print(f"The average profit/loss change between months in the dataset is: {currencychangetotal}.")
    print(f"The greatest increase from one month to another was in {highdate} for a gain of {currencyhigh}.")
    print(f"The greatest decrease from one month to another was in {lowdate} for a loss of {currencylow}.")


