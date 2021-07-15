import requests
from bs4 import BeautifulSoup

#Gets the request link and gets the content
recieved = requests.get("https://www.billboard.com/charts/hot-100").content
soup = BeautifulSoup(recieved, "html.parser")

#Prints the title and converts it to text
print("Top 10 Songs (Scraping from " + soup.title.text + ")\n----------------------------------------------------------")
counter = 1

#Finds where the song title is displayed and the artists are displayed
holder1 = soup.find_all('span', {'class': 'chart-element__information__song text--truncate color--primary'})
holder2 = soup.find_all('span', {'class': 'chart-element__information__artist text--truncate color--secondary'})

#Iterates through both and prints the top 10 songs along with the artists
for song, artists in zip(holder1,holder2):
    if counter < 11:
        print(str(counter) + " " + song.text + " - " + artists.text)
        counter += 1
