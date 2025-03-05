# default argument
def wish(user = 'Guest', msg = 'Hi'):
    print(msg, user )


# Positional
wish('Anders')
wish('Tom', 'Hello')

# Keyword args
wish(user = "Bob")
wish(msg = "Hello", user = "Bob")
wish()


