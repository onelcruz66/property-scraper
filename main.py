import requests
import pandas
from bs4 import BeautifulSoup

r = requests.get("https://www.century21.com/real-estate/fredericksburg-va/LCVAFREDERICKSBURG/")
c = r.content

soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("div",{"class":"property-card-primary-info"})
find_all = all[0].find("a",{"class":"listing-price"}).text.replace("\n","").replace(" ","")

list_prop = []
for item in all:
    property = {}
    property['address']=item.find_all("div", {"class": "property-address"})[0].text.replace("\n", "").replace(" ", "")
    property['city']=item.find_all("div", {"class": "property-city"})[0].text.replace("\n", "").replace(" ", "")
    property['price']=item.find("a", {"class": "listing-price"}).text.replace("\n", "").replace(" ", "")
    try:
        property['beds']=item.find("div", {"class": "property-beds"}).find("strong").text
    except:
        property['beds']=None
    try:
        property['baths']=item.find("div", {"class": "property-baths"}).find("strong").text
    except:
        property['baths']=None
    try:
        property['half_baths']=item.find("div", {"class": "property-half-baths"}).find("strong").text
    except:
        property['half_baths']=None
    try:
        property['sqft']=item.find("div", {"class": "property-sqft"}).find("strong").text
    except:
        property['sqft']=None

    list_prop.append(property)
df = pandas.DataFrame(list_prop)

df.to_csv("fdxg_properties.csv")