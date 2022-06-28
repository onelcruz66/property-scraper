import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.century21.com/real-estate/fredericksburg-va/LCVAFREDERICKSBURG/")
c = r.content

soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("div",{"class":"property-card-primary-info"})
find_all = all[0].find("a",{"class":"listing-price"}).text.replace("\n","").replace(" ","")

for item in all:
    print(item.find("a",{"class":"listing-price"}).text.replace("\n","").replace(" ",""))
    print(item.find_all("div",{"class":"property-address"})[0].text.replace("\n","").replace(" ",""))
    print(item.find_all("div",{"class":"property-city"})[0].text.replace("\n","").replace(" ",""))
    try:
        print(item.find("div",{"class":"property-beds"}).find("strong").text)
    except:
        print(None)
    try:
        print(item.find("div",{"class":"property-baths"}).find("strong").text)
    except:
        print(None)
    try:
        print(item.find("div",{"class":"property-half-baths"}).find("strong").text)
    except:
        print(None)
    try:
        print(item.find("div",{"class":"property-sqft"}).find("strong").text)
    except:
        print(None)

    print(" ")
