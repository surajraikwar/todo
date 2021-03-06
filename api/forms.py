from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account, Task
from django.contrib.auth import authenticate


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email',
                  'password1', 'password2')

class AddTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title',)


class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid:
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Credentials')
