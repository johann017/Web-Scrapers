import requests
from bs4 import BeautifulSoup

#Gets the request url and gets the contents of the awards page
recieved = requests.get('https://www.five9.com/about/awards').content
soup = BeautifulSoup(recieved, "html.parser")

#Finds where all the awards are listed and gets each award and prints it
for i in soup.find_all('h4',{'class':'mt-3 pt-1 mb-2 pb-2 font-weight-bold text-primary'}):
    print(i.text.strip())
