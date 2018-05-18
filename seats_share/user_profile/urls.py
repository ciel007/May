from django.urls import path
from . import views

app_name = 'user_profile'
urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('profile_edit', views.profile_edit, name='edit_my_profile')
]