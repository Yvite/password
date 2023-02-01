import random
import string

def generate_password(length):
    password = []
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.punctuation))
    for i in range(length-3):
        password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
    random.shuffle(password)
    password = ''.join(password)
    return password

password = generate_password(10)

print("Generated password:", password, " ")
