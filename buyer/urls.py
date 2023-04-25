from django.urls import path
from buyer.views import index,buyer

urlpatterns = [
    # path('buyer/<int:id>/',index,name='buyer'),
    path('buyer/',index,name='buyer'),
    path('savebuyer/',buyer,name='buyersave')

]