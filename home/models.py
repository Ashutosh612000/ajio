from django.db import models
# from phone_field import PhoneField


class Home_Detail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField(null=True, blank=True)
    # files = models.FileField(null= True , blank=True)

    class Meta:
        verbose_name_plural = ("Home")

    def __str__(self):
        return self.name
    

# Create your models here.
