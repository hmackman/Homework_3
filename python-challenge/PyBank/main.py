#open the csv first
import os
import csv


# #Path to the csv-file
budget_data_csv = os.path.join("../PyBank","budget_data.csv")

# #opening and reading the csvfile
with open(budget_data_csv, newline="") as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")    
    
    totalMonths = 0
    NetPL = 0
    header = next(csvreader)

    for row in csvreader:
            
        totalMonths = totalMonths + 1
        NetPL = NetPL + int(row[1])
          
print("Financial Analysis")
print("------------------")
print(f'Total Months: {totalMonths}')
print(f'Total: ${NetPL}')




with open(budget_data_csv, newline="") as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")    
    
    totalMonths = 0
    NetPL = 0
    header = next(csvreader)
    first_row = next(csvreader)

    for row in csvreader:
        
        totalMonths = totalMonths + 1
        NetPL = NetPL + int(row[1])
        netchange = 0
        prevnet = int(first_row[1])
        netchange = int(row[1]) - prevnet
        
        
    

print(f'Average: ${netchange/totalMonths}')


with open(budget_data_csv) as csvfile:

   csvreader = csv.reader(csvfile,delimiter=",")

   # skip csv header
   next(csvreader)

   # deltas of month-to-month profits/losses
   PLChanges = []

   # previous profit/loss
   prev_pl = 0

   for row in csvreader:

       # get profit/loss datum
       pl = int(row[1])

       # calculate the delta
       pl_change = pl - prev_pl

       # append the value to the master list
       PLChanges.append(pl_change)

       # store current profit/loss for next iteration's calculation
       prev_pl = pl


#print(PLChanges)
decrease = min(PLChanges)
increase = max(PLChanges)

increaseMonthIndex = 0
decreaseMonthIndex = 0

for x in PLChanges:
    if x == increase:
        increaseMonthIndex = str(PLChanges.index(x))
    if x == decrease:
        decreaseMonthIndex = str(PLChanges.index(x))


# print(increaseMonthIndex)
# print(decreaseMonthIndex)
# print(PLChanges)

with open(budget_data_csv) as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")

   # skip csv header
    next(csvreader)
    months = []
    

    for row in csvreader:
        months.append(row[0])

increaseMonth = months[int(increaseMonthIndex)]
decreaseMonth = months[int(decreaseMonthIndex)]
print(f'Greatest Increase in Profits: {increaseMonth} (${increase})')
print(f'Greatest Decrease in Profits: {decreaseMonth} (${decrease})')



       
            
        





# # 1. Write the purpose of the process.
# # 2. Write the initial steps that set the stage for functions.
# # 3. Write only one statement per line.
# # 4. Write what you mean, not how to program it.
# # 5. Use standard programming structures.
# # 6. Use blocks to structure steps.
# # 7. Add comments if necessary.