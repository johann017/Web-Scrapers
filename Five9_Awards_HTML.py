import requests
#import urllib.request
from bs4 import BeautifulSoup
recieved = requests.get('https://www.five9.com/about/awards').content
soup = BeautifulSoup(recieved, "html.parser")
for i in soup.find_all('h4',{'class':'mt-3 pt-1 mb-2 pb-2 font-weight-bold text-primary'}):
    print(i.text.strip())
