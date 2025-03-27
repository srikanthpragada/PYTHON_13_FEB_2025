from datetime import date, datetime, timedelta

f = open('players.txt', 'rt')
players = []
for line in f.readlines():
    parts = line.strip().split(',')
    if len(parts) < 2:
        continue

    name = parts[0]
    try:
        dob = datetime.strptime(parts[1], '%d-%m-%Y')
        td = (datetime.today() - dob)  # timedelta
        age = td.days // 365
        #print(name, age)
        players.append( (name, age))

    except Exception as ex:
        pass

f.close()

# sort by name - first element of tuple
for name, age in sorted(players):
    print(f"{name:10} {age:2}")

# sort by age - second element of tuple
for name, age in sorted(players, key = lambda t : t[1]):
    print(f"{name:10} {age:2}")


