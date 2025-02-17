# Calculate net price by taking price
# Add 15% tax

price =float(input("Enter price :"))
tax = price * 15 / 100

net_price = price + tax

print(f"Price     :  {price:8.2f}")
print(f"+ Tax     :  {tax:8.2f}")
print(f"Net Price :  {net_price:8.2f}")


