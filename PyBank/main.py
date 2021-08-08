import os
import csv

# Declare Variables
months_sum = 0
profit_loss_total = 0
avg_change = 0
g_increase_date = ''
g_increase_val = 0
g_decrease_date = ''
g_decrease_val = 0

# open CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    
    csv_header = next(csvreader)
    
    for row in csvreader:
        my_date = row[0]
        # if statement
        if (my_date):
            months_sum = months_sum + 1
        
        profit_loss = int(row[1])
        # if statement2
        if (profit_loss):
            profit_loss_total = profit_loss_total + profit_loss

            # check if contains the greatest increase/decrease
            if (profit_loss > g_increase_val):
                g_increase_date = my_date
                g_increase_val = profit_loss
            elif (profit_loss < g_decrease_val):
                g_decrease_date = my_date
                g_decrease_val = profit_loss
        
    # find average change
    if (months_sum > 0):
        avg_change = round(profit_loss_total / months_sum, 2)

# print the results
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {months_sum}')
print(f'Total: ${profit_loss_total}')
print(f'Average Change: ${avg_change}')
print(f'Greatest Increase in Profits: {g_increase_date} (${g_increase_val})')
print(f'Greatest Decrease in Profits: {g_decrease_date} (${g_decrease_val})')

# create file with results
results = 'Financial Analysis.txt'

with open(results, 'w') as text:
    # add line break
    text.write('Financial Analysis\n')
    text.write('----------------------------\n')
    text.write(f'Total Months: {months_sum}\n')
    text.write(f'Total: ${profit_loss_total}\n')
    text.write(f'Average Change: ${avg_change}\n')
    text.write(f'Greatest Increase in Profits: {g_increase_date} (${g_increase_val})\n')
    text.write(f'Greatest Decrease in Profits: {g_decrease_date} (${g_decrease_val})')