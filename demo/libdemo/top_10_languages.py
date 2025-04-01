import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.tiobe.com/tiobe-index/")
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')
top20_table = soup.find(id="top20")

if top20_table is None:
    print('Sorry! Could not find top20 table!')
    exit()


#print(top20_table.text)
table_body = top20_table.find("tbody")
#print(table_body)

rows  = table_body.find_all("tr")
for row in rows[:10]:
    cols = row.find_all("td")
    name = cols[4].text
    rank = float(cols[5].text.strip("%"))
    print(f"{name:25} {rank:5.2f}%")








