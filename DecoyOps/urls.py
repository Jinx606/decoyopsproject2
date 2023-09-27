from django.urls import path, include, re_path
from . import views


# Here we have the app name
app_name = 'DecoyOps'

# The url paths below have the names and which pages they will render once calling on the views page. The only difference is that the first page you encounter is the login page and if chosen, the registration page. once logged in, the other links will become active and a logout option will appear in the navbar
urlpatterns = [
    path('info/', views.info_view, name='info'),
    path('work/', views.work_view, name='work'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.user_registration, name='register'),
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('UNNATURAL/', views.UNNATURAL_view, name='UNNATURAL'),
    path('ADIDAS/', views.ADIDAS_view, name='ADIDAS'),
    path('superskin/', views.SUPERSKIN_view, name='SUPERSKIN'),
    path('TEXTILES/', views.TEXTILES_view, name='TEXTILES'),
]

