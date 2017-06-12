import random


def get_password(password_length=13):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pw_length = password_length
    pw = ""

    for i in range(pw_length):
        next_index = random.randrange(len(alphabet))
        pw = pw + alphabet[next_index]

    # replace 1 or 2 characters with a number
    for i in range(random.randrange(1, 5)):
        replace_index = random.randrange(len(pw) // 2)
        pw = pw[0:replace_index] + str(random.randrange(10)) + pw[replace_index + 1:]

    # replace 1 or 2 letters with an uppercase letter
    for i in range(random.randrange(1, 5)):
        replace_index = random.randrange(len(pw) // 2, len(pw))
        pw = pw[0:replace_index] + pw[replace_index].upper() + pw[replace_index + 1:]

    return pw
