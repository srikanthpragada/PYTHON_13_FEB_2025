import requests

response  = requests.get("https://restcountries.com/v3.1/all")
countries = response.json()
sorted_countries = sorted(countries, key = lambda c : c['area'], reverse= True)

for c in sorted_countries[:10]:
    name = c['name']['common']
    population = int(c['population'])
    area = float(c['area'])
    print(f"{name:30} - {population:10}   - {area:10.0f}")



