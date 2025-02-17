# Take price and display discount

price = int(input("Enter price :"))

if price > 10000:
    discount = price * 20 // 100
else:
    discount = price * 10 // 100

print(f'Discount = {discount}')
