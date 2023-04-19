from django.contrib import admin
from seller.models import Seller_Detail

class seller_admin(admin.ModelAdmin):
        model = Seller_Detail
        list_display=["seller_name","seller_item_type"]


# Register your models here.

admin.site.register(Seller_Detail,seller_admin)