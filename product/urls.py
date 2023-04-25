from django.urls import path
from product.views import index,delete_data,update_data

urlpatterns = [
    path('product/',index,name="product"),
    path('delete/<int:id>/',delete_data,name='daletedata'),
    path('<int:id>/',update_data,name='updatedata'),
]