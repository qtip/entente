"""entente_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from register.views import register
from services.views import add_server, index_server, index_channel, detail_channel, index_services

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", register, name="register"),
    path('', include("django.contrib.auth.urls")),
    path("add_server/", add_server, name="add_server"),
    path("<int:pk>/", index_channel, name="index_channel"),
    path("servers", index_server, name="index_server"),
    path("", index_services, name="index_services"),
    path("<int:server_pk>/<int:channel_pk>", detail_channel, name="detail_channel"),
]
