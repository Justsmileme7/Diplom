from django.urls import path, re_path
from .views import MainPageView


urlpatterns = [
    path('', MainPageView.as_view(), name='mainpage'),


]