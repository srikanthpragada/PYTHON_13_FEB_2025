# Assume d may have any one of the following two structures
#d = {'name': 'Jack', 'email': 'jack@gmail.com'}
d = {'firstname': 'Scott'}

match d:
    case {'name': user}:
        print("Found name : ", user)
    case {'firstname': user}:
        print("Found firstname : ", user)
    case _:
        print("Sorry! Didn't find user")
