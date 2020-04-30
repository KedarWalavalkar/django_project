from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, primary_key=True)
    contact = models.BigIntegerField()
    password = models.CharField(max_length=30)

# forms.CharField(max_length=30,widget=forms.PasswordInput)
class Category(models.Model):
    pro_category_name=models.CharField(max_length=30, primary_key=True)

class Products(models.Model):
    pro_name = models.CharField(max_length=30)
    # pro_id = models.IntegerField(primary_key=True)
    pro_price = models.DecimalField(max_digits=8,decimal_places=2)
    pro_dscript = models.TextField(max_length=50)
    pro_category_name=models.ForeignKey(Category,on_delete=models.CASCADE)

class Carts(models.Model):
    email=models.ForeignKey(Users,on_delete=models.CASCADE)
    pro_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    count=models.IntegerField(default=1)
    
# class Orders(models.Model):
#     email=models.ForeignKey(Users,on_delete=models.CASCADE)
#     total_bill=models.IntegerField()
#     date=models.DateField()
#     status=models.CharField(max_length=30)
    
# class Address(models.Model):
#     pin=models.IntegerField()
#     state=models.CharField(max_length=30)
#     email=models.ForeignKey(Users,on_delete=models.CASCADE)
    


    
