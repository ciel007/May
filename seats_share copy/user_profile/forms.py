from django import forms
from .models import User, UserProfile

GENDER_CHOICES = (
		(u'M', u'Male'),
		(u'F', u'Female'),
		)

class UserProfileForm(forms.ModelForm):
	gender = forms.ChoiceField(label=u'user_gender', choices=GENDER_CHOICES)

	def __int__(self, *args, **kwargs):
		super(UserProfileForm, self).__init__(*args, **kwargs)
		self.fields['gender'].choices = GENDER_CHOICES

	class Meta:
		model = UserProfile
		fields = ("name", "age", "major", "hometown", "phoneNum")
		widgets = {'name': forms.TextInput(attrs={"id":"nameEdit", "style":"background-color: whitesmoke", "class":"form-control", "type":"name", "placeholder":"Name"}),
		'age': forms.TextInput(attrs={"id":"ageEdit", "style":"background-color: whitesmoke", "class":"form-control", "type":"age", "placeholder":"Age"}),
		#'gender': forms.TextInput(attrs={"class":"form-control", "style":"background-color: whitesmoke" "id":"genderEdit"}),
		'major': forms.TextInput(attrs={"id":"majorEdit", "style":"background-color: whitesmoke", "class":"form-control", "type":"major", "placeholder":"Major"}),
		'hometown': forms.TextInput(attrs={"id":"hometownEdit", "style":"background-color: whitesmoke", "class":"form-control", "type":"hometown", "placeholder":"Hometown"}),
		'phoneNum': forms.TextInput(attrs={"id":"phoneEdit", "style":"background-color: whitesmoke", "class":"form-control", "type":"phone", "placeholder":"Phone Number"}),
		}

		

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ("email",)