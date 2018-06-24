import os
import csv

budget_data ='c:\\temp\\budget_data.csv'

file_path = os.path.join('c:\\temp\\budget_data.csv')
with open(file_path,newline='') as csvfile:
    budget_data = csv.reader(csvfile, delimeter=",")
next(budget,none)
for row in csvdata:
 #school
    months.append(row[0])
    revenue.append(int(row[1]))

budgetmonths = budgetmonths + 1
#def
totalrevenue = totalrevenue + int(row[1])
       # def       
       if budgetmonths >= 1:
            change = change + (int(row[1]) - int(prevrow[1]))
        if (int(row[1]) - int(prevrow[1]))>greatestinc:
            greatestinc = int(row[1])-int(prevrow[1])
            greatestincdate = str(row[0])
        if (int(row[1]) - int(prevrow[1]))<greatestdec:
            greatestdec = int(row[1])-int(prevrow[1])
            greatestdecdate = str(row[0])
        prevrow = row
        totalmonths = budget1months + budget2months
avgchange = int(change/totalmonths)

print("Total Months: " + str(totalmonths) )
print("Total Revenue: $" + str(totalrevenue))
print("Average Revenue Change: $" + str(avgchange))
print("Greatest Increase in Revenue: " + str(greatestincdate) + " ($" + str(greatestinc) + ")")
print("Greatest Decrease in Revenue: "+ str(greatestdecdate) + " ($" + str(greatestdec) + ")")


           



#if os.path.exists(budget_data):
