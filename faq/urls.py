from django.urls import path, include
from faq.views import (faq)

urlpatterns = [
    path('', faq, name='faq-home'),
]
