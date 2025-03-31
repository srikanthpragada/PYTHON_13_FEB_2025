import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.tiobe.com/tiobe-index/")
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')
top20_table = soup.find(id="top20")
print(top20_table.text)


