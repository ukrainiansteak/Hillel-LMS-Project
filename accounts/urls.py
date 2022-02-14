from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from accounts.views import AccountRegister, AccountLogin, AccountEdit, ChangePasswordView, ChangePasswordDoneView

app_name = 'accounts'

urlpatterns = [
    path('register', AccountRegister.as_view(), name='register'),
    path('login', AccountLogin.as_view(), name='login'),
    path('profile', AccountEdit.as_view(), name='profile'),
    path('logout', LogoutView.as_view(next_page=reverse_lazy('accounts:login')),
         name='logout'),
    path('password', ChangePasswordView.as_view(), name='change_password'),
    path('password_changed', ChangePasswordDoneView.as_view(),
         name='password_change_done'),
    ]
