def wish(*names, message = 'Hi'):
    for n in names:
        print(message, n)


wish('Scott', 'Larry', 'Mike', message = "Hello")
wish('Tom', 'Bill')
