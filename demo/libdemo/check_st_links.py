import requests
from bs4 import BeautifulSoup

WEBSITE = "https://www.srikanthtechnologies.com/"
def make_absolute_link(link):
    if link.startswith("http"):
        return link
    else:
        return WEBSITE + link.strip("/")

def is_link_valid(link):
    response = requests.get(link)
    if response.status_code != 200:
        return False
    else:
        return True

response = requests.get("https://www.srikanthtechnologies.com/")
if response.status_code != 200:
    print('Sorry! Could not get details!')
    exit()

contents = response.text
soup = BeautifulSoup(contents, 'html.parser')
links = soup.find_all('a')
print("Links count = ", len(links))

unique_links = set()
for a in links:
    # check whether href is present for <a>
    if 'href' in a.attrs:
        href = a['href']
        if href != '#':
            unique_links.add( make_absolute_link(href))


print("Unique Links :", len(unique_links))

# List of broken links
print("Broken Links")
print("============")
for link in unique_links:
    if not is_link_valid(link):
        print(link)






