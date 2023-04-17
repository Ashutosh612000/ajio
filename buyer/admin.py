from django.contrib import admin
from buyer.models import Buyer_Detail

class Buyer_Admin(admin.ModelAdmin):
    model = Buyer_Detail
    list_displayed =["Name", "Email",]
  
admin.site.register(Buyer_Detail,Buyer_Admin,)
# admin.site.register(Author, AuthorAdmin)
# Register your models here.
