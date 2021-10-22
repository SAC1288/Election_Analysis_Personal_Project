import csv

reader = csv.reader(open('Data/president_county_candidate.csv'))

next(reader)


candidates_and_parties = []
for row in reader:
    candidates_and_parties.append(row(2))
    candidates_and_parties.append(row(2))
    
        
print(candidates_and_parties)











        


for row in reader:
    if row == 'Joe Biden':
        candidates.append(row)

      
# print('Total Votes: ',votes)