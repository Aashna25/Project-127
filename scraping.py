from bs4 import BeautifulSoup
import requests
import csv
import time
import pandas as pd

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page= requests.get(START_URL)
print(page)
soup = BeautifulSoup(page.text, "html.parser")
star_table = soup.find("table")
temp_list = []
table_rows = star_table.find_all("tr")
for tr in table_rows:
    td= tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)

name_list = []
distance_list = []
mass_list = []
radius_list = []

for i in range(1,len(temp_list)):
    name_list.append(temp_list[i][1])
    distance_list.append(temp_list[i][3])
    mass_list.append(temp_list[i][5])
    radius_list.append(temp_list[i][6])

df2=pd.DataFrame(list(zip(name_list,distance_list, mass_list, radius_list)),columns=["star_name","distance","mass","radius"])

print(df2)
df2.to_csv("stars.csv")
    
