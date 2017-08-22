import os
import csv
import string
import collections
import sys


town=input("which Town?    ")

csvpath = os.path.join('Resources', 'election_data_'+ town +'.csv')

# Specify the file to write to
sys.stdout = open('election_result_'+ town +'.txt', 'w')

voter = 0 
cand_list =[] 
cnt1 = {} 


# Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
     
    next(csvreader, None)
    #  Each row is read as a row
    for row in csvreader:
        # print each row is an array
        #print(row) #each row is an array
        #print the first coloume. 0 is the index
  
        voter = voter + 1
        cand =row[2]
        cand_list.append(cand)

    print("Election Results")
    print("---------------------------------")
    print("Total Votes:   ",voter)    
    from collections import Counter
    cnt1=Counter(cand_list)

    for key,value in cnt1.items():
        print(key + ':  ',"{0:.0f}%".format(value/voter * 100),\
                    "(" + str(value) + ")")

    
    maxx = max(cnt1.values())
    winner = [x for x,y in cnt1.items() if y ==maxx]
    print("---------------------------------")
    print("Winner:   ", ', '.join(winner[0:len(winner)+1]))
    print("---------------------------------")