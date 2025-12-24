from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu/', null=True, blank=True)
    category = models.CharField(max_length=20,choices=[('coffee', 'Coffee'), ('snack', 'Snack')],default='coffee')
    def _str_(self):
        return self.name


    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    item = models.ForeignKey(MenuItem,on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

