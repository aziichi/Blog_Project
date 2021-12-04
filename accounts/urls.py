from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import signUpView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signup/', signUpView, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', PasswordResetView.as_view(template_name='registration/pass_reset.html'), name="password_reset"),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='registration/pass_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/pass_reset_confirm.html'), name="password_reset_confirm"),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='registration/pass_reset_complete.html'), name="password_reset_complete"),

]