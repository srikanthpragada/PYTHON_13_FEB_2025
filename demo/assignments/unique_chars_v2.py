# take 5 names and display unique chars

names = ['Joe', 'James', 'Jack', 'Mark','Anders']
chars = "".join(names)    # Join all strings to make a big string
unique_chars = set(chars)  # Take only unique chars
print( sorted(unique_chars)) # Print chars after sorting

