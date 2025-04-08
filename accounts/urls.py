from django.urls import path
from accounts.views import PodcastLoginView, logout_view, RegistrationView

urlpatterns = [
    path('login/', PodcastLoginView.as_view(), name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', RegistrationView.as_view(), name="register") 
]