"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
import app.views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
	path('register/', app.views.userregisterPage, name="userregister"),
	path('login/', app.views.userloginPage, name="userlogin"),  
	path('logout/', app.views.logoutUser, name="logout"),
    path("", app.views.home, name="home"),
    path("home/", app.views.userhome, name="user-page"),
    path("contacts/", app.views.contact, name="contact"),
    path("create/", app.views.create, name="create"),
    path("update/<str:pk>/", app.views.update, name="update"),
    path("delete/<str:pk>/", app.views.delete, name="delete")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)