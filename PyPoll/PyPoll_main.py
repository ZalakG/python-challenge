# import the os module which allows to create file path across operating system
import os

# module for reading CSV files
import csv

# path for election_data.csv file 
election_csv = os.path.join("C:/Zalak-Course/Module3_Challenge/python-challenge/PyPoll/Resources/election_data.csv")
election_csv_Output = os.path.join("C:/Zalak-Course/Module3_Challenge/python-challenge/PyPoll/Resources/analysis_data.csv")

#election_csv_Output = os.path.join("C:\Zalak-Course\Module3_Challenge\python-challenge\PyPoll\Analysis\election_result.txt")

# Open and read election_data CSV file
with open(election_csv, newline = "")as csvfile:

    # Specifies delimiter and variables in the file that holds contents

    csvreader = csv.reader(csvfile, delimiter = ',')

    # count total number of votes cast (skip the header row in counting)

    csv_header = next(csvreader)
    election_data = list(csvreader)
    total_row = len(election_data)
   

    # count numnber of candidates who received votes in "Candidate" column by creating list
    candidate_list = list()
    totalcandidate = list()
    can_vote_count = 0
    cad_votes_map = {}
    
    with open("C:/Zalak-Course/Module3_Challenge/python-challenge/PyPoll/Analysis/election_result.txt", "w")as file:
        line1 = f"\n\nElection Results \n\n-------------------------------------------\n\nTotal Votes: {total_row}\n\n-------------------------------------------\n"
        print(line1)
        file.write(line1)
        for row in range (2,total_row):
            candidate = election_data[row][2]
            totalcandidate.append(candidate)
            if candidate in cad_votes_map:
                cad_votes_map[candidate] = cad_votes_map[candidate] + 1
            else:
                cad_votes_map[candidate] = 1

        for candie in cad_votes_map:
            val = f"{candie} : {format(cad_votes_map[candie] / total_row * 100, '.3f')}%  {cad_votes_map[candie]}\n "
            print(val)
            file.write(val)
        print(f"-------------------------------------------\n\n")
        file.write(f"-------------------------------------------\n\n")

        line2 = f"Winner: {max(cad_votes_map, key=cad_votes_map.get)}\n\n-------------------------------------------\n\n"
        print(line2)
        file.write(line2)
        file.close()
        
            
        
        
        
        #totalcandidate.append(candidate)
        

    #     if candidate not in candidate_list:
    #         candidate_list.append(candidate)
    # can_name = str(candidate_list)
   

    # calculate number of votes per candidate won and percentage of votes per candidate by creating variables: C_list(Candidate list) and totalvote
    # totalvote = 0  
    # C_list = {}  
    # for r in csvreader:
    #     totalvote += 1
    #     C_name = r[2]
    #     if C_name in C_list:
    #         C_list[C_name] += 1
    #     else:
    #         C_list[C_name] = 1

    # 
   # for candidate, votes in C_list.items():



