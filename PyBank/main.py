import os
import csv
import string
import collections
import sys
 
rev_inc_list = []
t_rev = 0
t_months = 0
t_rev_inc = 0
rev_inc = 0
pre_rev = 0
cur_rev = 0
max_inc_rev = 0
min_inc_rev = 0

# Output file
sys.stdout = open('PyBank.out', 'w')

csvpath = os.path.join('Resources', 'budget_data_1.csv')

# Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip read Header 
    next(csvreader, None)
    #  Each row is read as a row
    for row in csvreader:
          
        t_rev = t_rev + int(row[1])

        t_months = t_months + 1
        
        cur_rev=int(row[1]) 
        rev_inc = cur_rev - pre_rev      
        if rev_inc > max_inc_rev:
            max_inc_rev = rev_inc
            max_rev_month = row[0]
        elif rev_inc < min_inc_rev:
            min_inc_rev = rev_inc
            min_rev_month = row[0] 

        rev_inc_list.append(rev_inc)
        pre_rev = cur_rev
        
    #skip the first rev increase because there is no previous value
    rev_inc_list.pop(0)

    #print(rev_inc_list)
    avg_inc =round(sum(rev_inc_list) / float(len(rev_inc_list)))

    print("-------------------------------------")
    print("Financial Analysis")
    print("-------------------------------------")
    print("Total Months:   ", t_months)
    print("Total Revenue: $" + str(t_rev))
    print("Average Revenue Change: $" + str(avg_inc) )    
    print("Greatest Increase in Revenue:",\
             max_rev_month,  "($" + str(max_inc_rev) + ")")
    print("Greatest Decrease in Revenue:",\
             min_rev_month,  "($" + str(min_inc_rev)  + ")")
   
             
    

 

    