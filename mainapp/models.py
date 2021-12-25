from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=150)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        if not self.parent:
            return self.name
        else:
            return f"{self.parent} --> {self.name}"

    def get_children(self):
        if self.children:
            return self.children.all()
        return False


class Product(models.Model):
    title = models.CharField(max_length=150)
    descriptions = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    owner = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title

    def get_model_name(self):
        return self.__class__.__name__.lower()


class Image(models.Model):
    image = models.ImageField(upload_to='media/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')





