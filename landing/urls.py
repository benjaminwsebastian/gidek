from django.urls import path, include
from landing.views import (home)

urlpatterns = [
    path('', home, name='website-home'),
]
