# import tools
import csv
import os
import numpy as np 

# create pathway to file
election_data_file = os.path.join("raw_data", "election_data_1.csv")

# create output file and results to it 
text_path = os.path.join("Output", "election_results.txt")
f = open(text_path, "w")

# print first part of summary to file and terminal
print("Election Results", file=f)
print("Election Results")
print("------------------------", file=f)
print("-------------------------")

# open file and create data lists
with open(election_data_file) as election_data:
        reader = csv.reader(election_data)

        # use next to skip title row
        # intilize null lists
        next(reader) 
        voter = []
        county = []
        candidate = []

        # loop through data and add each row of data to appropreiate list
        for row in reader:
            county.append(row[1])
            voter.append(row[0])
            candidate.append(row[2])

        # set variable and calculate total number of voters
        total_voters = len(voter)

# print to summary in terminal and file 
print("Total Votes: ", str(total_voters), file=f)
print("Total Votes: ", str(total_voters))
print("-------------------------", file=f)
print("-------------------------")

# define unique function to compile list of candidate names
def unique(candidate):
 
    # intilize a null list
    candidate_list = []

    # traverse for all elements
    for x in candidate:
        # check if exists in unique_list or not
        if x not in candidate_list:
            candidate_list.append(x)
    # traverse through candidate list to find total votes and vote percentage for each candidate
    for x in candidate_list:
        name_total = candidate.count(x)
        percent = name_total/total_voters * 100

        # print results for each element in list to summary in terminal and file
        print(str(x), ": ", str(percent), "%", " (", str(name_total), ")", file=f)
        print(str(x), ": ", str(percent), "%", " (", str(name_total), ")")

# run function 
unique(candidate)

# use numpy tool to find most frequent element in candidate list
(values,counts) = np.unique(candidate,return_counts=True)
ind=np.argmax(counts)

# print most frequent element to summary in terminal and file 
print("Winner: ", values[ind], file=f)  
print("Winner: ", values[ind])  

print("-------------------------", file=f)
print("-------------------------")



  

