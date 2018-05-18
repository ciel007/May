from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, RegisterForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django_otp.oath import TOTP
import time
from django.core.mail import send_mail
from django.views import View
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)


# def user_login(request):
# 	if request.method == "POST":
# 		if not request.POST.get('remember'):
# 			request.session.set_expiry(0)

# the remember me in model are not connected with the view
class UserLoginView(LoginView):
	form_class = LoginForm

	def form_valid(self, form):
		if self.request.POST.get('remember_me') is None:
			print(self.request.POST.get('remember_me'))
			# print(self.request.session.get_expiry_date())
			self.request.session.set_expiry(0)
			# print(self.request.session.get_expiry_date())
		auth_login(self.request, form.get_user())
		return HttpResponseRedirect(self.get_success_url())

	# def remember_me(self):
	# 	user_login(self.request)
	# 	return HttpResponseRedirect(self.get_success_url())


class UserRegisterView(View):
	secret_key = b"12345678900987654321"
	now = int(time.time())
	totp = TOTP(key=secret_key, step=60, t0=now, digits=6, drift=1)
	code = totp.token()

	def get(self, request):
		form = RegisterForm()
		# verification_form = VerificationForm()
		return render(request, 'registration/register.html', {"form":form})

	def post(self, request):
		print(request.POST)
		if 'ver_code_send' in request.POST:
			request.POST = request.POST.copy()
			request.POST.pop('ver_code_send')
			form = RegisterForm(request.POST)
			print(request.POST)
			if form.is_valid():
				print("11111111111111")
				subject = "Verification Code"
				message = "Here is the verification: " + str(self.code) + " (valid in 60s)"
				send_mail(subject, message, '905486274@qq.com', [form.cleaned_data.get('email')], fail_silently=False)
				return HttpResponse()
				# return render(request, 'registration/register.html')
			else:
				# verification_form = VerificationForm()
				return render(request, 'registration/register.html', {"form":form})

		elif 'register_submit' in request.POST:
			#ver_form = VerificationForm(request.POST)
			request.POST = request.POST.copy()
			request.POST.pop('register_submit')
			form = RegisterForm(request.POST)
			if form.is_valid():
				print("is valid")
				print(isinstance(form.cleaned_data.get('token'), str))
				print(isinstance(self.code, int))
				if self.totp.verify(self.code, tolerance=1):
					print("got cleaned data")
					user = form.save()
					return render(request, 'seats_info/main_function_page.html')

				else:
					return HttpResponse()
			else:
				return HttpResponse("")

		else:
			form = RegisterForm()
			# verification_form = VerificationForm()
			return render(request, 'registration/register.html', {"form":form})

		
					
				










	