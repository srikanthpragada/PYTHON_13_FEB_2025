
def count_upper(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count


def count_digits(s):
    count = 0
    for c in s:
        if c.isdigit():
            count += 1

    return count