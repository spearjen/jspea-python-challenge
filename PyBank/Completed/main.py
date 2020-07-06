
#Import modules
import os
import csv

#Zero totals
total = 0
changetotal = 0
currenthighchange = 0
currentlowchange = 0

#Define file path
csvpath = os.path.join("..","Resources","budget_data.csv" )

#Read CSV file
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile)
    #Skip the header row 
    csvheader = next(csvreader)
    #Count number of lines in CSV file, and print info using f string
    lines = len(list(csvreader))
   
#Read CSV files
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile)
    #Skip the header row 
    csvheader = next(csvreader)
    #Iterate through rows and set initial values
    for row in csv.reader(csvfile):
        bestdate = row[0]
        worstdate = row[0]
        old = float(row[1])
        total = float(row[1])
        oldchange =float(0)    
        #Iterate through rows, finding total change
        for row in csv.reader(csvfile):
            total = float(row[1]) + total
            new = float(row[1])
            change = new-old
            old = new
            changetotal = float(changetotal) + float(change)
            #Iterate through rows, finding greatest change and least change (month to month)
            if currenthighchange >= change:
                currenthighchange = currenthighchange
            else:
                currenthighchange = change
                bestdate = str(row[0])
            
            if currentlowchange <= change:
                currentlowchange = currentlowchange
            else:
                currentlowchange = change
                worstdate = str(row[0])
        #Format to currency   
        #Currency formatting info found at kite.com
        currencytotal = "${:,.2f}".format(total)
        currencychangetotal = "${:,.2f}".format(changetotal/(lines-1))     
        currencyhigh = "${:,.2f}".format(currenthighchange)
        currencylow = "${:,.2f}".format(currentlowchange)

    data = (f"There are {lines} months of data contained in the dataset.\n"
            f"The total profit/loss for all months and years in the dataset is: {currencytotal}.\n"
            f"The average profit/loss change between months in the dataset is: {currencychangetotal}.\n"
            f"The greatest increase from one month to another was in {bestdate} for a gain of {currencyhigh}.\n"
            f"The greatest decrease from one month to another was in {worstdate} for a loss of {currencylow}.")
   
    #Print to screen
    print(data)

    #Print to file
    outputfile = os.path.join ("..","Analysis","bank_final.txt")
    with open(outputfile, "w") as bank_final:
        bank_final.write(data)
    
    #completed
        