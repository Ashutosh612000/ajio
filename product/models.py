from django.db import models



class Product_list(models.Model):
    product_name = models.CharField(max_length=50)

    def __str__(self):
        return self.product_name
    

class Grocery(models.Model):
    grocery_item = (
        ('Staples','Steples'),
        ('Snacks & Beverages','Snacks & Beverages'),
        ('Packaged Food','Packaged Food'),
        ('Personal & Baby Care','Personal & Baby Care'),
        ('Household Care','Household Care'),
        ('Dairy & Eggs','Dairy & Eggs'),
        ('Home & Kitchen','Home & Kitchen'),
    )
    
    product_name = models.ForeignKey("Product_list", on_delete=models.CASCADE)
    grocery_item = models.CharField(max_length=20,choices=grocery_item)
    available = models.BooleanField()
    
    def __str__(self):
        return self.grocery_item



class Electronics(models.Model):
    product_name = models.ForeignKey("Product_list",on_delete=models.CASCADE)
    electronic_item = models.CharField(max_length=50)

    def __str__(self):
        return self.electronic_item
    


class Mobile(models.Model):
    electronic_item = models.ForeignKey("Electronics", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    mobile_model = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name
    










# class Product_Detail(models.Model):
#     # company_product =(
#     #     ("Mobile","mobile"),
#     #     ("tv","tv"),
#     #     ("ac","ac"),
#     # )
#     product_company = models.CharField(max_length=50, blank=True, null=True)
#     # company_name = models.CharField(max_length=100,)
#     # company_product = models.CharField(max_length=50,choices=company_product)
#     # product_model_name = models.CharField(max_length=100 , null= True, blank=True)
#     available = models.BooleanField()
#     number_of_product = models.IntegerField()
#     # product_image = models.ImageField(upload_to='media')

#     def __str__(self):
#         return self.product_company
    

# class Phone(models.Model):
#     # company_product =(
#     #     ("Mobile","mobile"),
#     #     ("tv","tv"),
#     #     ("ac","ac"),
#     # )
#     product_company = models.ForeignKey(Product_Detail,on_delete=models.CASCADE)
#     model = models.CharField(max_length=50)
#     price = models.CharField(max_length=50)
#     product_image = models.ImageField(upload_to='media')

#     # company_name = models.CharField(max_length=100,)
#     # company_product = models.CharField(max_length=50,choices=company_product)
#     # product_model_name = models.CharField(max_length=100 , null= True, blank=True)
#     # available = models.BooleanField()
#     # number_of_product = models.IntegerField()

#     def __str__(self):
#         return self.model
# # Create your models here.



