from django.shortcuts import render
from .forms import PasswordForm
import random
import string

def password_generator(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data['length']
            password = generate_password(length)
            message = "Password generated successfully!"
        else:
            password = None
            message = "Invalid form input."
    else:
        form = PasswordForm()
        password = None
        message = ""
    return render(request, "index.html", {"form": form, "password": password, "message": message})


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
