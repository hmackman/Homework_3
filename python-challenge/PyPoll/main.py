#import os and csv to open/read the csvfile
import os
import csv

#open and read the csv file - complete

election_data = os.path.join("../PyPoll","election_data.csv")


with open (election_data, newline="") as csvfile:


    csvreader = csv.reader(csvfile,delimiter=",")    
    header = next(csvreader)
    #need to get total number of rows minus header to get total votes cast
    totalVotes = 0
    votesKhan = 0
    votesCorrey = 0
    votesLi = 0
    votesOTooley = 0
    #list for candidates
    candidates = []
    for row in csvreader:
        #gets total votes
        totalVotes = totalVotes + 1

        #puts column 3 in a list
        candidates.append(row[2])

        #determines total vote count for each candidate
        if row[2] == "Khan":
            votesKhan = votesKhan +1
        elif row[2] == "Correy":
            votesCorrey = votesCorrey + 1
        elif row[2] == "Li":
            votesLi = votesLi + 1
        elif row[2] == "O'Tooley":
            votesOTooley = votesOTooley + 1

        #print(row)



#unique candidates
uniquecandidates = set(candidates)
#determines what percentage of total votes each candidate had
percentageWonKhan = '{0:.3f}'.format((votesKhan/totalVotes)*100)
percentageWonCorrey = '{0:.3f}'.format((votesCorrey/totalVotes)*100)
percentageWonLi = '{0:.3f}'.format((votesLi/totalVotes)*100)
percentageWonOTooley = '{0:.3f}'.format((votesOTooley/totalVotes)*100)

#Determines who has most votes
if votesKhan > votesCorrey or votesLi or votesOTooley:
    Winner = "Khan"
elif votesCorrey > votesKhan or votesLi or votesOTooley:
    Winner = "Correy"
elif votesLi > votesKhan or votesCorrey or votesOTooley:
    Winner = "Li"
elif votesOTooley > votesKhan or votesCorrey or votesLi:
    Winner = "O'Tooley"


#print results
print("Election Results")
print("----------------")
print(f'Total Votes: {totalVotes}')
print("----------------")
print(f'Khan: {percentageWonKhan}%  ({votesKhan})')
print(f'Correy: {percentageWonCorrey}%  ({votesCorrey})')
print(f'Li: {percentageWonLi}%  ({votesLi})')
print(f"O'Tooley: {percentageWonOTooley}%  ({votesOTooley})")
print("----------------")
print(f'Winner: {Winner}')
print("----------------")
#print(uniquecandidates)


# 1. Write the purpose of the process.
# 2. Write the initial steps that set the stage for functions.
# 3. Write only one statement per line.
# 4. Write what you mean, not how to program it.
# 5. Use standard programming structures.
# 6. Use blocks to structure steps.
# 7. Add comments if necessary.