from django.urls import path
from buyer.views import index

urlpatterns = [
    path('buyer/',index)
]