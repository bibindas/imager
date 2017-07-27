from django import forms

class signupForm(forms.Form):
    username= forms.CharField(max_length=10)
    email = forms.EmailField()
    password= forms.CharField(max_length=100)
    confirmpassword= forms.CharField(max_length=100)
