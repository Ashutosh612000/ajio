from django.db import models

class Seller_Detail(models.Model):

    item_type = (
        ("Electronic", "Electronic"),
        ("clothing", "Clothing"),
        
    )

    seller_name = models.CharField(max_length=100)
    seller_item_type = models.CharField(max_length=100,choices=item_type)
    item_image = models.ImageField()

# Create your models here.
