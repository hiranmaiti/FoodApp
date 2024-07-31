from django.db import models

# Create your models here.

class Items(models.Model):
    # def __self__(self):
    #     return self.item_name
    item_name = models.CharField(max_length=122)
    item_desc = models.CharField(max_length=122)
    item_price = models.IntegerField()
    item_image = models.URLField(max_length=200, blank=True, null=True)
