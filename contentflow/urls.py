from django.urls import path
from . import views


urlpatterns = [
    path('', views.TestView.as_view()),
    path('auth/user-change/', views.UserProfileView.as_view(), name='user-change')
]    