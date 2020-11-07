from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
        }
    
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
