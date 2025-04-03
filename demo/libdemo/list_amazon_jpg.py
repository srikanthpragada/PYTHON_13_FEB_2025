
import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.amazon.in/")

soup = BeautifulSoup(resp.text, 'html.parser')
images = soup.find_all("img")

for img in images:
    if 'src' in img.attrs:
        src = img['src']
        if src.endswith(".jpeg") or src.endswith(".jpg"):
            print(src)




