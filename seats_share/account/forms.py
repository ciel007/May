from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput

class LoginForm(AuthenticationForm):
	username = UsernameField(max_length=254, widget=forms.TextInput(attrs={"type":"email", "class":"form-control", "id":"exampleInputEmail1", "placeholder":"Email address", "name":"email"}))
	password = forms.CharField(widget=forms.TextInput(attrs={"type":"password", "class":"form-control", "id":"exampleInputPassword1", "placeholder":"Password", "name":"password"}))
	remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"name": "remember", "type": "checkbox", "value": "Remember Me"}))

class RegisterForm(UserCreationForm):
	#email_address = forms.EmailField()
	token = forms.CharField(max_length=6, required=False, widget=forms.TextInput(attrs={"class":"form-control", "type":"text", "placeholder":"Verification Code"}))

	class Meta:
		model = User
		fields = ["email"]
		widgets = {'email': forms.TextInput(attrs={"type":"email", "class":"form-control", "id":"exampleInputEmail1", "placeholder":"Email address", "name":"email"}),
		# 'username': forms.TextInput(attrs={"style":"background-color: whitesmoke", "class":"form-control", "type":"text", "placeholder":"E-mail"}),
		}

	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		self.fields['password1'].widget = PasswordInput(attrs={"type":"password", "class":"form-control", "id":"exampleInputPassword1", "placeholder":"Password"})
		self.fields['password2'].widget = PasswordInput(attrs={"type":"password", "class":"form-control", "id":"exampleInputPassword2", "placeholder":"Confirm Password"})
	
	#def send_email(self):


	# #override save() in UserCreationForm
	# def save(self, commit=True ):
	# 	user = super(RegisterForm, self).save(commit=False)
	# 	#user.email_address = self.cleaned_data["email_address"]
	# 	user.set_password(self.cleaned_data["password1"])
	
# class VerificationForm(forms.Form):
# 	token = forms.CharField(max_length=6, required=True, widget=forms.TextInput(attrs={"id":"code", "style": "background-color: whitesmoke", "class":"form-control", "type":"text", "placeholder":"verification code"}))

