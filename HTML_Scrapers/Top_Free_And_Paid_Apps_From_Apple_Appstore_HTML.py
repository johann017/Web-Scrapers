import requests
from bs4 import BeautifulSoup

#Gets the requested url and gets the contents of the page
recieved = requests.get('https://apps.apple.com/us/story/id1535572713').content
soup = BeautifulSoup(recieved, "html.parser")
print("Top Paid and Free App (via App Store)\n-------------------------------------")

#Finds where the paid and free apps are
for i in soup.find_all('h2', {'class':'section__headline'}):
    
    #Prints whether it's free or paid
    print(i.text.strip() + ":")
    counter = 1
    
    #Prints the apps under each section in the order it's displayed on the appstore
    for j in i.find_next().find_all('h3',{'class': 'truncate-single-line we-product-collection__item__product-name', 'dir': 'auto'}):
        print("\t" + str(counter) + " " + j.text.strip())
        counter += 1
