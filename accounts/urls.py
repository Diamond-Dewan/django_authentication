from django.urls import path, include
from accounts.views import UserRegister, UsersListView
urlpatterns = [
    path('', UsersListView.as_view(), name='index'),
    path('register/', UserRegister.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
