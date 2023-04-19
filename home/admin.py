from django.contrib import admin
from home.models import Home_Detail


class Home_Admin(admin.ModelAdmin):
    model =Home_Detail
    list_display = ["name","email"]
    


admin.site.register(Home_Detail, Home_Admin)
# Register your models here.
