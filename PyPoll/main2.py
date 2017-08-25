import os
import csv
import string
import sys

# Prompt input the town name then find the right datafile to use.
town=input("which Town? (Hillbilly or Somerset) ")

csvpath = os.path.join('Resources', 'election_data_'+ town +'.csv')

# Specify the file to write to
sys.stdout = open('election_result_'+ town +'.txt', 'w')

t_voter = 0 
cand_list =[] 
max_vote_count = 0 
voter_count = 0 


# Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
     
    next(csvreader, None)
    #  Each row is read as a row
    for row in csvreader:  
        t_voter = t_voter + 1
        cand = row[2]
        #print(cand)
        if cand not in cand_list:
                cand_list.append(cand)
        
    print("Electioncand_list Results")
    print("---------------------------------")
    print("Total Votes:",t_voter) 
      
      
     
for cand1 in cand_list:  
    voter_count = 0
    with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
        csvreader1 = csv.reader(csvfile, delimiter=',') 
        next(csvreader1, None)        
        for row in csvreader1: 
            item = row[2]
            if str(cand1) == str(item):
                voter_count = voter_count + 1
        print(str(cand1), str(round(voter_count/t_voter * 100, 3)) +"%",\
                    "(" + str(voter_count) + ")") 
        
        if voter_count > max_vote_count:
            max_vote_count = voter_count
            winner = str(cand1)
print("---------------------------------")
print("Winner:   ", winner)