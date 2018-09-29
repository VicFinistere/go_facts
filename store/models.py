"""Models used for the application"""
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    types = (
        (0, 'Girl'),
        (1, 'Boy'),
        (2, 'Other')
    )
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    gender = models.SmallIntegerField(choices=types, default='0', db_index=True)


class Product(models.Model):
    """Model use to stock products"""
    name = models.CharField(max_length=200)
    image = models.URLField()
    categories = models.TextField(max_length=1500)
    grade = models.CharField(max_length=5)
    nutriments = models.TextField(max_length=1500)
    code = models.CharField(max_length=30)


class Favorite(models.Model):
    """Model used to stock the favorites products of an user"""
    User = get_user_model()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default='', related_name='product')
    substitute = models.ForeignKey(Product, on_delete=models.CASCADE, default='', related_name='substitute')
