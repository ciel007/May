from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import User
from .models import UserProfile
from .forms import UserProfileForm, UserForm
from django.http import HttpResponse

@login_required
def profile(request):
	user = User.objects.get(email=request.user.email)
	print(request)
	print(request.user.email)
	try:
   		userprofile = UserProfile.objects.get_or_create(user=user)	
	except:
		pass
	return render(request, "user_profile/profile.html", {"user":user, "userprofile":userprofile})
					
@login_required
def profile_edit(request):
	user = User.objects.get(email=request.user.email)
	userprofile = UserProfile.objects.get(user=request.user)
	print(request.method)
	if request.method == "POST":
		print("Here______________________")
		request.POST = request.POST.copy()
		request.POST.pop("email")
		#user_form = UserForm(request.POST)
		userprofile_form = UserProfileForm(request.POST)
		print(request.POST)
		if userprofile_form.is_valid():
			#user_cd = user_form.cleaned_data
			userprofile_cd = userprofile_form.cleaned_data
			#print(user_cd["email"])
			#user.email = user_cd['email']
			userprofile.name = userprofile_cd['name']
			userprofile.age = userprofile_cd['age']
			userprofile.gender = userprofile_cd['gender']
			userprofile.major = userprofile_cd['major']
			userprofile.hometown = userprofile_cd['hometown']
			userprofile.phoneNum = userprofile_cd['phoneNum']
			#user.save()
			userprofile.save()
			user = User.objects.get(email=request.user.email)
			userprofile = UserProfile.objects.get(user=request.user)
			return render(request, "user_profile/profile.html", {"user":user, "userprofile":userprofile})
		else:
			return HttpResponse("we are here")
		#return render(request, "searchseat/index.html")
	else:
		user_form = UserForm(instance=request.user)
		userprofile_form = UserProfileForm(initial={"name":userprofile.name, "age":userprofile.age, "gender":userprofile.gender, "major":userprofile.major, "hometown":userprofile.hometown, "phoneNum":userprofile.phoneNum})
		return render(request, "user_profile/profile_edit.html", {"user_form":user_form, "userprofile_form":userprofile_form})
		#return render(request, "profile/profile_edit.html", {"user":user, "userprofile":userprofile})
