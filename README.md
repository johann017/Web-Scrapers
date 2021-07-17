# Web-Scrapers

## Setup

To run `Billboard_Top_10_HTML.py`:
- `python Billboard_Top_10_HTML.py`

To run `Five9_Awards_HTML.py`:
- `python Five9_Awards_HTML.py`

To run `Top_Free_And_Paid_Apps_From_Apple_Appstore_HTML.py`:
- `python Top_Free_And_Paid_Apps_From_Apple_Appstore_HTML.py`

To view dataset for `Kaggle_Netflix_Top_10_CSV.py`:
- `https://github.com/johann017/Web-Scrapers/blob/b7c0e00593c4175bcc608096639572c5c0e609b7/CSV_Scrapers/netflix_list.csv`

To view dataset for `Kaggle_2019_DOJ_crimes_By_Race_CSV.py`:
- `https://github.com/johann017/Web-Scrapers/blob/b7c0e00593c4175bcc608096639572c5c0e609b7/CSV_Scrapers/2019_DOJ_crimes_by_Race.csv`


## Description

- ### HTML Web Scrapers

  - #### `Billboard_Top_10_HTML.py`
    - The purpose of this file is to go to the Billboard Top 100 songs and retrieve the top 10 in that list along with the artists.

  - #### `Five9_Awards_HTML.py`
    - The purpose of this file is to go to the Five9's award page and retrieve the all the awards won by Five9.
    
  - #### `Top_Free_And_Paid_Apps_From_Apple_Appstore_HTML.py`
    - This program goes to the top apps in the Apple appstore and scrapes the information off their website. This program recognizes the difference between the paid and free apps and scrapes them accordingly.
    
- ### CSV Scrapers
  - #### `Kaggle_Netflix_Top_10_CSV.py`
    - This program analyzes the dataset downloaded off from Kaggle. It takes and returns the Top 10 Netflix shows from the dataset.
 
  - #### `Kaggle_2019_DOJ_crimes_By_Race_CSV.py`
    - This program analyzes the dataset downloaded off from Kaggle. It calculates the race with the highest reported number of crimes in a year and returns what percent of total crimes were committed by this group.
