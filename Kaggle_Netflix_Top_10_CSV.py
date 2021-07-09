import csv

import pandas as pd
df = pd.read_csv (r"C:\Users\jantisseril\Downloads\netflix_list.csv")
counter = 1
for row in df.get('title'):
    if counter < 11:
        print(str(counter) + " " + row)
        counter += 1