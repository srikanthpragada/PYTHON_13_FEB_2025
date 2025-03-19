
a = input("Enter a number :")
try:
    n =  int(a)
    print(100 / n)
except ValueError as ex:
    print('Invalid Number :', ex)
# except ZeroDivisionError :
#     print('Zero is not valid number here!')
finally:
    print("Finally")


print('Done')


