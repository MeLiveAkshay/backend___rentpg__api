from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('colleg_project.page.page__url')),  # Correct as long as this is your app's path
]

