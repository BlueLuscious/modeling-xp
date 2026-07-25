from django.urls import path
from authy.views.index_view import IndexView
from authy.views import LogOutView, LogInView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login/', LogInView.as_view(), name="login"),
    path('logout/', LogOutView.as_view(), name="logout"),
]
