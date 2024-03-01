from django.db import models
# Swagger

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_ref = models.TextField()
    product_title = models.TextField()
    product_slug = models.TextField()
    product_category = models.TextField()
    product_at = models.DateTimeField(auto_now=True)

