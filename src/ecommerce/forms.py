from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control", 
                "placeholder":"Enter your Full Name"
                    }
                  )
              )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class":"form-control", 
                "placeholder":"Enter your Email"
                    }
                  )
             )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":"form-control", 
                "placeholder":"Enter your Message"
                    }
                  )
             )
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "kcau.ac.ke" in email:
            raise forms.ValidationError("Please use your KCA University email")
        return email
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class":"form-control", 
                  }
                  )
             )
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "kcau.ac.ke" in email:
            raise forms.ValidationError("Please use your KCA University email")
        return email

class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField( label="Confirm password", widget=forms.PasswordInput)
   
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username


    
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password2 != password:
            raise forms.ValidationError("Passwords must match.")
        return data

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class":"form-control", 
                    }
                  )
             )
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "kcau.ac.ke" in email:
            raise forms.ValidationError("Please use your KCA University email")
        return email
    