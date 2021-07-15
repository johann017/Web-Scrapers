import csv
import pandas as pd

#Gets the csv from where it is in the computer
df = pd.read_csv (r"C:\Users\jantisseril\Downloads\2019_DOJ_crimes_by_Race.csv")

#Keeps a record of total crimes committed by each race.
race = {'w':0,'aa':0,'ai':0,'a':0}
total = 0

#Goes column by column and adds the crimes up by each group
for col in df:
    for row in df.get(col):
        if col == 'All races':
            total += row
        elif col == 'White':
            race['w'] += row
        elif col == 'Black':
            race['aa'] += row
        elif col == 'American Indian':
            race['ai'] += row
        elif col == 'Asian':
            race['a'] += row
        else:
            continue
            
#Gets the highest number or crimes committed
maxval = max(race.values())
print("According to the 2019_DOJ_crimes_by_Race.csv, out of " + str(total) + " crimes, the group with the highest crime rate were ", end='')

#Goes through each element in race and gets the group to be printed
for r in race:
    if race[r] == maxval:
        if r == 'w':
            print("Whites",end='')
        elif r == 'aa':
            print("African Americans",end='')
        elif r == 'ai':
            print("Asian Americans",end='')
        elif r == 'a':
            print("Asians",end='')
        else:
            continue
            
#Prints the percent of the total amount of crime committed by this group.
print(" and made up " + str((maxval/total)*100) + "% of all crimes.")
