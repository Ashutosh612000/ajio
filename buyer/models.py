from django.db import models


class Buyer_Detail(models.Model):
    Name = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=10)
    # Date_of_birth = models.DateField()
    Email = models.EmailField()

    class Meta:
        verbose_name_plural = ("Buyer")

    def __str__(self):
        return self.Name
    

class Buyer_city(models.Model):
    Buyer_Detail = models.ManyToManyField(Buyer_Detail)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)

