import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Delare variables
total_votes = 0
candidates = {}

# open csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader) # store the header: ['Voter ID', 'County', 'Candidate']

    # checking each row
    for row in csvreader:
        candidate = row[2]
        if candidate:
           
            total_votes = total_votes + 1
           
            votes_for = candidates.get(candidate)
            if (votes_for):
                candidates[candidate] = votes_for + 1
            else:
                candidates[candidate] = 1    

output_file = 'Election Results.txt'

# final analysis
with open(output_file, 'w') as text:
    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {total_votes}')
    print('-------------------------')
    text.write('Election Results\n')
    text.write('-------------------------\n')
    text.write(f'Total Votes: {total_votes}\n')
    text.write(f'-------------------------\n')
    winner = ''
    for possible_winner in candidates:
        final_vote = candidates[possible_winner]
        percentage = (final_vote / total_votes) * 100 
        percentage_str = f"{percentage:.3f}"    
        print(f'{possible_winner}: {percentage_str}% ({final_vote})')
        text.write(f'{possible_winner}: {percentage_str}% ({final_vote})\n')
        if winner == '':
            winner = possible_winner    
        elif final_vote > candidates[possible_winner]:
            winner = possible_winner
    print('-------------------------')
    print(f'Winner: {winner}')
    print('-------------------------')
    text.write(f'-------------------------\n')
    text.write(f'Winner: {winner}\n')
    text.write(f'-------------------------\n')