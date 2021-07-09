import requests
from bs4 import BeautifulSoup
recieved = requests.get('https://apps.apple.com/us/story/id1535572713').content
soup = BeautifulSoup(recieved, "html.parser")
print("Top Paid and Free App (via App Store)\n-------------------------------------")
for i in soup.find_all('h2', {'class':'section__headline'}):
    print(i.text.strip() + ":")
    counter = 1
    for j in i.find_next().find_all('h3',{'class': 'truncate-single-line we-product-collection__item__product-name', 'dir': 'auto'}):
        print("\t" + str(counter) + " " + j.text.strip())
        counter += 1