from django.urls import path
from seller.views import index

urlpatterns = [
    path('seller/',index)
]