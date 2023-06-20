from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('update_profile_submit/', views.update_profile_submit, name='update_profile_submit'),
]
