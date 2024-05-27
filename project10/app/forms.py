from django import forms
from django.contrib.auth.models import User

class userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']
        help_texts={'first_name':'enter your first name','username':'select a unique user'}
        widgets={'password':forms.PasswordInput}