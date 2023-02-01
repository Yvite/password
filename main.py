import random
import string

charlength = int(input("How many characters do you want in your password? "))
if charlength < 6:
    print("Password must be at least 6 characters long.")
    charlength = int(input("How many characters do you want in your password? "))
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

password = generate_password(charlength)

print('Generated password:"', password,'"')
