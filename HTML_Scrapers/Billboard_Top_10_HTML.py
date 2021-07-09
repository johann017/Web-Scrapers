import requests
from bs4 import BeautifulSoup
from csv import writer

recieved = requests.get("https://www.billboard.com/charts/hot-100").content
soup = BeautifulSoup(recieved, "html.parser")
print("Top 10 Songs (Scraping from " + soup.title.text + ")\n----------------------------------------------------------")
counter = 1
holder1 = soup.find_all('span', {'class': 'chart-element__information__song text--truncate color--primary'})
holder2 = soup.find_all('span', {'class': 'chart-element__information__artist text--truncate color--secondary'})
for song, artists in zip(holder1,holder2):
    if counter < 11:
        print(str(counter) + " " + song.text + " - " + artists.text)
        counter += 1
