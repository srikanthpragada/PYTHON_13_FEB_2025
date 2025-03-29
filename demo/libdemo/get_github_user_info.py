import requests

user = input("Enter username :")

response = requests.get(f"https://api.github.com/users/{user}")
if response.status_code != 200:
    print("Sorry! Could not get details!")
    exit()

details = response.json()

print(f"Name     : {details['name']}")
print(f"Location : {details['location']}")
print(f"Company  : {details['company']}")


