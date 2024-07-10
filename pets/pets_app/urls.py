from django.urls import path, re_path
from .views import MainPageView, PetsPageView, FeedbackPageView


urlpatterns = [
    path('', MainPageView.as_view(), name='mainpage'),
    path('/pets/<int:id>/', PetsPageView.as_view(), name='petpage'),
    path('/feedback/', FeedbackPageView.as_view(), name='feedback'),


]