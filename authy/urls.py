from django.urls import path
from authy.views import LogOutView, LogInView

urlpatterns = [
    path('login/', LogInView.as_view(), name="login"),
    path('logout/', LogOutView.as_view(), name="logout"),
]
