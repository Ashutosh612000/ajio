from django.contrib import admin
from product.models import Product_list,Grocery,Electronics,Mobile

# class Product_Admin(admin.ModelAdmin):
#     model = Product_Detail
#     list_display = ["company_name","company_product","number_of_product","available"]

class Product_list_Admin(admin.ModelAdmin):
    model = Product_list
    list_display = ['product_name']
# Register your models here.

admin.site.register(Product_list,Product_list_Admin)
admin.site.register(Grocery)
admin.site.register(Electronics)
admin.site.register(Mobile)
