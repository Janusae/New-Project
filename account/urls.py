from django.urls import path
from . import views
urlpatterns = [
    path('', views.RegisterView.as_view() , name = "register"),
    path('login', views.LoginView.as_view() , name = "login"),
    path('logout', views.LogoutView.as_view() , name = "logout"),
    path('forget', views.ForgetView.as_view() , name = "forget"),
    path('reseat-pass/<code>', views.ReseatView.as_view() , name = "reseat_pass"),
    path("actve-code/<str:code>" , views.ActveCodeView.as_view() , name = "actve-code")
]