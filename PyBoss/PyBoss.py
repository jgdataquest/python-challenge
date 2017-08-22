import os
import csv
import string 
import datetime
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

csvpath1 = os.path.join('Resources', 'employee_data1.csv')
csvpath2 = os.path.join('Resources', 'employee_data2.csv')

# Specify the file to write to
output_path1 = os.path.join('Resources', 'employee_data3.csv')
output_path2 = os.path.join('Resources', 'employee_data4.csv')


# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path1, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Emp ID','First Name', 'Last Name','DOB', 'SSN','State'])

# Improved Reading using CSV module
with open(csvpath1) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #found = False
    #user_choice=input("what movie you select?")
    firstrow =next(csvreader)
    #  Each row is read as a row
    for row in csvreader:
        # print each row is an array
        #print(row) #each row is an array
        #print the first coloume. 0 is the index
        #print(row[0]) 
        tb=[]
        y =row[1].split(' ')
        DOB=row[2]
        r2= (DOB[8:10] + DOB[4:7]+ "-" + DOB[0:4] )
        from datetime import datetime
        r21=datetime.strptime(r2, "%d-%m-%Y")
        SSN=row[3]
        r3=( "***-**" + SSN[6:11] )
        r4=row[4]
        if r4 in us_state_abbrev.keys():
            r4=us_state_abbrev[r4]
        tb.append (row[0])
        tb.extend(y)
        tb.append(r2)
        #tb.append(r21)
        tb.append(r3)
        tb.append(r4)
        #print(tb)    

        # Write the first row (column headers)
        with open(output_path1, 'a', newline='') as csvfile:
             # Initialize csv.writer
             csvwriter = csv.writer(csvfile, delimiter=',') 
             csvwriter.writerow(tb)

# use another way to do the same with the second file

with open(csvpath2) as csvfile: 

    # CSV reader specifies delimiter and variable that holds contents
    csvreader2 = csv.reader(csvfile, delimiter=',')
    
    firstrow =next(csvreader2)
    empid2 = []
    fname2 = []
    lname2 = []
    DOB2 = []
    SSN2 = []
    State2 = []
    #  Each row is read as a row
    for row in csvreader2:
        # print each row is an array
        #print(row) #each row is an array
        #print the first coloume. 0 is the index
        #print(row[0]) 
        empid2.append(row[0])

        name2 =row[1].split(' ')
        fname2.append(name2[0])
        lname2.append(name2[1])

        z2 =row[2].split('-')
        birth2=(z2[2] + "-" + z2[1]+ "-" + z2[0])
        DOB2.append(birth2)

        s2=row[3]
        social2=( "***-**" + s2[6:11] )
        SSN2.append(social2)

        St2=row[4]
        if St2 in us_state_abbrev.keys():
             St22=us_state_abbrev[St2]
        State2.append(St22) 

    Zipper=zip(empid2, fname2, lname2, DOB2, SSN2, State2)

    with open(output_path2, 'w', newline='') as datafile:
             # Initialize writer
        writer = csv.writer(datafile)

    # Write the header row
        writer.writerow(['Emp ID','First Name', 'Last Name','DOB', 'SSN','State'])
        writer.writerows(Zipper)
    

        

    
        
        
