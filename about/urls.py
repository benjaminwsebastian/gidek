from django.urls import path, include
from about.views import (team, plan)

urlpatterns = [
    path('our-plan/', plan, name='about-plan'),
    path('our-team/', team, name='about-team'),
]