from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    # path('', views.index, name='index'),
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/register/', views.UserRegisterView.as_view(), name='register'),
]
