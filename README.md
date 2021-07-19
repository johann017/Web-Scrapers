# Web-Scrapers

## Description

- ### HTML Web Scrapers

  - #### `Billboard_Top_10_HTML.py`
    - #### Overview: 
      - This program goes through the Billboard Top 100 songs and retrieves the top 10 in that list along with the artists.

  - #### `Five9_Awards_HTML.py`
    - #### Overview: 
      - This program goes to the Five9's award page and retrieves the all awards won by Five9.
    
  - #### `Top_Free_And_Paid_Apps_From_Apple_Appstore_HTML.py`
    - #### Overview: 
      - This program goes through the top apps in the Apple appstore and scrapes the information off their website. This program recognizes the difference between the paid and free apps and scrapes them accordingly.
    
- ### CSV Scrapers
  - #### `Kaggle_Netflix_Top_10_CSV.py`
    - #### Overview: 
      - Analyzes the dataset downloaded from Kaggle. It reads and returns the Top 10 Netflix shows from the dataset.
 
  - #### `Kaggle_2019_DOJ_crimes_By_Race_CSV.py`
    - #### Overview: 
      - Analyzes the dataset downloaded off from Kaggle and calculates the race with the highest reported number of crimes in a year and returns the percent of total crimes that were committed by this group.

## Setup
- Install [GitHub CLI](https://cli.github.com/) and connect it with GitHub account
- Open up Git CMD
- Run `gh repo clone johann017/Web-Scrapers` in the command line

`Billboard_Top_10_HTML.py`:
- To run this, type the following in to the command line:
  ```
  python Billboard_Top_10_HTML.py
  ```

`Five9_Awards_HTML.py`:
- To run this, type the following in to the command line:
  ```
  python Five9_Awards_HTML.py
  ```

`Top_Free_And_Paid_Apps_From_Apple_Appstore_HTML.py`:
- To run this, type the following in to the command line:
  ```
  python Top_Free_And_Paid_Apps_From_Apple_Appstore_HTML.py
  ```

To view dataset for `Kaggle_Netflix_Top_10_CSV.py`:
- `https://github.com/johann017/Web-Scrapers/blob/b7c0e00593c4175bcc608096639572c5c0e609b7/CSV_Scrapers/netflix_list.csv`

To view dataset for `Kaggle_2019_DOJ_crimes_By_Race_CSV.py`:
- `https://github.com/johann017/Web-Scrapers/blob/b7c0e00593c4175bcc608096639572c5c0e609b7/CSV_Scrapers/2019_DOJ_crimes_by_Race.csv`
