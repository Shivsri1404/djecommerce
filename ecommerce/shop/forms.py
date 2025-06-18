# from django import forms
# from .models import ContactUs

# class ContactUsForm(forms.ModelForm):
#     class Meta:
#         model = ContactUs
#         fields = ['name', 'email', 'phone', 'subject', 'question']

# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password1', 'password2']

# class CustomLoginForm(AuthenticationForm):
#     username = forms.CharField(label='Username')
#     password = forms.CharField(widget=forms.PasswordInput)
