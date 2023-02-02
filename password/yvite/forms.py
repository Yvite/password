from django import forms

class PasswordForm(forms.Form):
    length = forms.IntegerField(label='Password Length', min_value=6,)