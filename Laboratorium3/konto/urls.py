from django.urls import path
from . import views
from .views import SignUpView, PasswordsChangeView
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('signup/', SignUpView.as_view(), name='signup'),

   
    path('change-password/', PasswordsChangeView.as_view(template_name = "registration/change_password.html"), name='change_password'),
    path('change_password_done/', views.changed, name='change_password_done'),

   
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset_form'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]