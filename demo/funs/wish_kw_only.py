# Keyword only args
def wish(*, user, message):
    print(message, user)


#wish('Larry', 'Hi')
wish(message = 'Hello', user = 'Larry')
