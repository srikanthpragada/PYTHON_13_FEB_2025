# calculate net amount with 30% discount for qty > 2 and 20% otherwise
# Add 8% tax

qty = int(input("Enter qty :"))
price = int(input("Enter price :"))
amount = qty * price

if qty > 2:
    discount = amount * 30 // 100
else:
    discount = amount * 20 // 100

after_discount = amount - discount
tax = after_discount * 8 // 100
net_amount = after_discount + tax

print(f"Amount          : {amount:8}")
print(f"- Discount      : {discount:8}")
print(f"After Discount  : {after_discount:8}")
print(f"+ Tax           : {tax:8}")
print(f"Net Amount      : {net_amount:8}")