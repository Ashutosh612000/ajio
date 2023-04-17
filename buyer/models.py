from django.db import models

class Buyer_Detail(models.Model):
    
    Name = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=10)
    Date_of_birth = models.DateField()
    Email = models.EmailField()

    class meta:
        varbose_name = 'buyer'

    def __str__(self):
        return self.Name
    

# Create your models here.
