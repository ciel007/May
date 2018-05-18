from django.urls import path
from . import views

app_name = 'seats_info'

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page'),
]
