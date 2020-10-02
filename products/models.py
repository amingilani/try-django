from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(
        default="this is cool! I'm making incremental migrations based off of a model"
    )
