import csv

reader = csv.reader(open('Data/president_county_candidate.csv'))

next(reader)

#going to find number of counties that included each candidate
candidates_and_parties = {}
candidates_votes = {}
candidates_wins = {}
total_counties = 0 

for row in reader:
    candidate = row[2]
    votes = int(row[4])
    total_counties += 1

    if candidate not in candidates_and_parties.keys():
        candidates_and_parties[candidate] = 0
        candidates_votes[candidate] = 0
        candidates_wins[candidate] = 0

    candidates_and_parties[candidate] += 1
    candidates_votes[candidate] += votes

    if row[5] == "TRUE":
        candidates_wins[candidate] += 1
        
        
# for candidate in candidates_and_parties:
#     print(candidate,': ',candidates_wins[candidate])

output= f'''
=======ELECTION=ANALYSIS======
Total Counties: {total_counties}


'''


print(output)

#going to find number of votes for each candidate







        


for row in reader:
    if row == 'Joe Biden':
        candidates.append(row)

      
# print('Total Votes: ',votes)