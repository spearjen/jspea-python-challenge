#Import modules
import os
import csv

#Set path
csvpath = os.path.join("..","Resources","election_data2.csv" )

#Read CSV file
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile)
    #Skip the header row 
    csvheader = next(csvreader)
    #Count number of lines in CSV file, and print info using f string
    lines = len(list(csvreader))
    print(f"The number of votes cast was: {lines}.")
   
#Read CSV files
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile)
    #Skip the header row 
    csvheader = next(csvreader)
    #Iterate through rows and set initial values