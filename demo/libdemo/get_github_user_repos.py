import requests

user = input("Enter username :")

response = requests.get(f"https://api.github.com/users/{user}/repos")
if response.status_code != 200:
    print("Sorry! Could not get details!")
    exit()

repos = response.json()

for repo in repos:
    print(f"{repo['name']}")
    print(f"{repo['description']}")
    print('-' * 80)



