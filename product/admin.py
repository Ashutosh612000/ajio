from django.contrib import admin
from product.models import Product_list,Grocery,Electronics,Mobile

# class Product_Admin(admin.ModelAdmin):
#     model = Product_Detail
#     list_display = ["company_name","company_product","number_of_product","available"]

class Product_list_Admin(admin.ModelAdmin):
    model = Product_list
    list_display = ['product_name']

class Grocery_Admin(admin.ModelAdmin):
    model = Grocery
    list_display = ['product_name','grocery_item','available']


class Electronics_admin(admin.ModelAdmin):
    model = Electronics
    list_display = ['electronic_item']


class Mobile_Admin(admin.ModelAdmin):
    model = Mobile
    list_display = ['electronic_item','company_name','mobile_model']
# Register your models here.

admin.site.register(Product_list,Product_list_Admin)
admin.site.register(Grocery,Grocery_Admin)
admin.site.register(Electronics,Electronics_admin)
admin.site.register(Mobile,Mobile_Admin)
