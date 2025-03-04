# default argument
def wish(user, msg = 'Hi'):
    print(msg, user )


wish('Anders')
wish('Tom', 'Hello')
wish(user = "Bob")
wish(msg = "Hello", user = "Bob")

