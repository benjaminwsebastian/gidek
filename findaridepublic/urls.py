from django.urls import path, include
from findaridepublic.views import (search)

urlpatterns = [
    path('find-a-ride/', search, name='search-home'),
]