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

    #Iterate through rows and find total number of votes
    #My concern is if there is another candidate in the list(there isn't, but hypothetically)...can I compile the list of unique names by iterating through the rows?
    for row in csvreader:
        vote = row[2]
        if vote == "Khan":
            Khan = Khan + 1
        elif vote == "Correy":
            Correy = Correy + 1
        elif vote == "Li":
            Li = Li + 1
        elif vote == "O'Tooley":
            OTooley = OTooley + 1
    
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

    #Print to screen
    print(f"Khan received {Khanpercentage} ({Khan}) of votes")
    print(f"Correy received {Correypercentage} ({Correy}) of votes")
    print(f"Li received {Lipercentage} ({Li}) of votes")
    print(f"O'Tooley received {OTooleypercentage} ({OTooley}) of votes")
    print("________________________________________________")

    #Find the winner
    #Find largest number in list info found at tutorialgateway.org
    votetotals = [Khan, Correy, Liper, OTooley]
    if (max(votetotals)) == Khan:
        print("Khan wins!!!")
    elif (max(votetotals)) == Correy:
        print ("Correy wins!!!")
    elif (max(votetotals)) == Li:
        print ("Li wins!!!")
    elif (max(votetotals)) == OTooley:
        print("O'Tooley wins!!!")
    
    #Print to csv
    #Issues: prints across columns instead of down rows; can't figure out how to say Khan wins! using the find largest value in list I did above
    data = [str(f"The total number of votes cast was: {lines}"),
            str("________________________________________________"),
            str(f"Khan received {Khanpercentage} ({Khan}) of votes"),
            str(f"Correy received {Correypercentage} ({Correy}) of votes"),
            str(f"Li received {Lipercentage} ({Li}) of votes"),
            str(f"O'Tooley received {OTooleypercentage} ({OTooley}) of votes"),
            str("________________________________________________"),
            str("Khan wins!!!")]
                
    outputfile = os.path.join ("..","analysis","poll_final.csv")
    with open(outputfile, "w") as poll_final:
        writer = csv.writer(poll_final)
        writer.writerow(data)
        
    