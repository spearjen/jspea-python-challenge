#Import modules
import os
import csv

#Zero totals
Khan = 0
Correy = 0
Li = 0
OTooley = 0

#Set path
csvpath = os.path.join("..","Resources","election_data.csv" )

#Read CSV file
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile)
    #Skip the header row 
    csvheader = next(csvreader)
    #Count number of lines in CSV file, and print info using f string
    lines = len(list(csvreader))
    print(f"The total number of votes cast was: {lines}")
    print("________________________________________________")
   
#Read CSV files
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile)
    #Skip the header row 
    csvheader = next(csvreader)

    vote_dict = {}

    #Iterate through rows and find total number of votes
    for row in csvreader:
    #Create dictionary that keys unique candidates and finds vote totals at the same time; I learned this from awesome Justin in my tutoring session!
        try:
            vote_dict[row[2]] += 1
        except:
            vote_dict[row[2]] = 1
    #Stardard method iterating through rows
        vote = row[2]
        if vote == "Khan":
            Khan = Khan + 1
        elif vote == "Correy":
            Correy = Correy + 1
        elif vote == "Li":
            Li = Li + 1
        elif vote == "O'Tooley":
            OTooley = OTooley + 1
    print(vote_dict)
    
    #Find percentages
    Khanper = Khan/lines
    Correyper = Correy/lines
    Liper=Li/lines
    OTooleyper = OTooley/lines

    #Format percentages
    #Percentage formatting info found at kite.com
    Khanpercentage = "{:.0%}".format(Khanper)
    Correypercentage = "{:.0%}".format(Correyper)
    Lipercentage = "{:.0%}".format(Liper)
    OTooleypercentage = "{:.0%}".format(OTooleyper)

    #Find the winner
    #Find largest number in list info found at tutorialgateway.org
    votetotals = [Khan, Correy, Liper, OTooley]
    winner = ""
    if (max(votetotals)) == Khan:
        winner = "Khan "
    elif (max(votetotals)) == Correy:
        winner = "Correy "
    elif (max(votetotals)) == Li:
        winner = "Li "
    elif (max(votetotals)) == OTooley:
        winner = "O'Tooley "

#Print to file
    data = (f"The total number of votes cast was: {lines}\n"
            "________________________________________________\n"
            f"Khan received {Khanpercentage} ({Khan}) of votes\n"
            f"Correy received {Correypercentage} ({Correy}) of votes\n"
            f"Li received {Lipercentage} ({Li}) of votes\n"
            f"O'Tooley received {OTooleypercentage} ({OTooley}) of votes\n"
            "________________________________________________\n"
            f"{winner}wins!!!")
    #Print to screen
    print(data)
    
    #Print to csv
    outputfile = os.path.join ("..","Analysis","poll_final.txt")
    with open(outputfile, "w") as poll_final:
        poll_final.write(data)
        
    #completed