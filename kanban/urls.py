"""kanban URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from kanban import views

auth_url_patterns = [
    path("login/", views.LoginAPIView.as_view()),
    path("registration/", views.RegistrationAPIView.as_view())

]

api_url_patterns = [
    path("change-password/", views.ChangePasswordAPIView.as_view()),
    path("<int:id>/", views.LoggedInUserAPIView.as_view())
]

urlpatterns = [
    re_path('auth/', include(auth_url_patterns)),
    re_path('api/', include(api_url_patterns)),
    path('admin/', admin.site.urls),
]
