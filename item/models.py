from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    # to display the category name properly
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ('name',)  # this will order by names of the Category

    # here to show the name of the items in categories
    def __str__(self):  # In Flask we would use repr but here use str cuz it won't work
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)  # its upto user if he wants to keep the description or not
    price = models.FloatField()
    # for this image to work add the IMAGE_URL AND IMAGE_ROOT in settings
    # also it will automatically create the item images folder
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    # here we added the user first import it from django contrib auth models and then related_name is items and
    # on_delete is like when the user is deleted the items created by the user are also deleted
    created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

