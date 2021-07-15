import csv
import pandas as pd

#Gets the csv file where it is in the computer
df = pd.read_csv (r"C:\Users\jantisseril\Downloads\netflix_list.csv")

#Prints top 10 Netflix titles
counter = 1
for row in df.get('title'):
    if counter < 11:
        print(str(counter) + " " + row)
        counter += 1
