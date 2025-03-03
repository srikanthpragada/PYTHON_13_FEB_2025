data = [ ('Bob', 939393333), ('Larry', 38383333),
         ('Jack', 393939333), ('Scott', 393939332),
         ('Andy', 393939333), ('Larry', 8838383333)]

customers = {}

for entry in data:
    customers[entry[0]] = entry[1]

for name, mobile in sorted(customers.items()):
    print(name, mobile)






