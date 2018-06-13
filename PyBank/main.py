#import tools
import csv
import os


# create pathway to source data file 
budget_data_file = os.path.join("raw_data", "budget_data_1.csv")

# open file to read data
with open(budget_data_file) as revenue_data:
    reader = csv.reader(revenue_data)

    # use next to skip header row
    # initialize null lists
    next(reader)
    revenue = []
    date = []
    rev_change = []

    # traverse through rows 
    # append data to appropriate lists
    for row in reader:
        revenue.append(float(row[1]))
        date.append(row[0])

    # loop through revenue data list 
    for i in range(1, len(revenue)):
            # calculate difference between initial revenue and the following
            # add value to revenue change list
            rev_change.append(int(revenue[i]) - int(revenue[i-1])) 

            # calculate average revenue change
            avg_rev_change = sum(rev_change)/len(rev_change)
            avg_rev_change = round(avg_rev_change)

            # find the date for the max and min revenue changes using rev_change value as index 
            max_rev_change_date = date[rev_change.index(max(rev_change))]
            min_rev_change_date = date[rev_change.index(min(rev_change))]

# create output file
# create path to output file
text_path = os.path.join("Output", "revenue_results.txt")
f = open(text_path, "w")

# print results to file
print("Financial Analysis", file=f)
print("--------------------------------", file=f)
print("Total Months: ", str(len(date)), file=f)
print("Total Revenue: $", str(sum(revenue)), file=f)
print("Average Revenue Change: $", str(avg_rev_change), file=f)
print("Greatest Increase in Revenue: ", str(max_rev_change_date),"($", str(max(rev_change)),")", file=f)
print("Greatest Decrease in Revenue: ", str(min_rev_change_date),"($", str(min(rev_change)),")", file=f)

# print results to terminal 
print("Financial Analysis")
print("--------------------------------")
print("Total Months: ", str(len(date)))
print("Total Revenue: $", str(sum(revenue)))
print("Average Revenue Change: $", str(avg_rev_change))
print("Greatest Increase in Revenue: ", str(max_rev_change_date),"($", str(max(rev_change)),")")
print("Greatest Decrease in Revenue: ", str(min_rev_change_date),"($", str(min(rev_change)),")")