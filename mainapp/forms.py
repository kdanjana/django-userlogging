from django import forms


from .models import User


class UserSignUpForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    re_password = forms.CharField(widget=forms.TextInput(attrs={'type':'password'}))
    class Meta:
        model = User
        fields = ["user_name", "first_name", "last_name", "email", "password", "re_password"]
        error_messages = {"user_name" : {"required" : "Please enter user name"}}
        
        labels = {
              "user_name": "User Name",
              "first_name": "First Name",
              "last_name": "Last Name",
              "email": "Email",
              "password": "Enter Password",
              "re_password": "Re-Enter Password"
        }
        widgets = {
            "password": forms.TextInput(attrs={'type':'password'})
        }

    # this function will be used for the validation
    def clean(self):
        # data from the form is fetched using super function
        super(UserSignUpForm, self).clean()
        # extract the fields from the cleaned data
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        # conditions to be met 
        if password != re_password:
             self._errors['re_password'] = self.error_class(['Please enter password correctly.'])
        if len(password) > 20 or len(password) == 0:
             self._errors['password'] = self.error_class(['Password must contain maximum 20 characters.'])

        return self.cleaned_data


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["user_name", "password"]
        labels = {
            "user_name": "User Name",
            "password": "Password"
        }
        widgets = {
            "password": forms.TextInput(attrs={'type':'password'})
        }
        
        
       