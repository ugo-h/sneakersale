from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=150, db_index=True )
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(default='', blank=True, db_index=True)
    price = models.FloatField(blank=True, db_index=True)
    oldPrice = models.FloatField(default=0, blank=True, db_index=True)
    link = models.TextField(blank=True, db_index=True)
    img = models.TextField(blank=True, db_index=True)
    detailedImage = models.TextField(default='', db_index=True)
    brand = models.CharField(default='', max_length=150, db_index=True )
    last_update = models.DateTimeField(auto_now_add=True)

   

    def get_absolute_url(self):
        return reverse('product_details_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering =['price'.lower()]
    


class Brand(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    list_of_slugs = []
    def get_absolute_url(self):
        if not self.slug in self.list_of_slugs:
            self.list_of_slugs.append('+')
            self.list_of_slugs.append(self.slug)
        else:
            self.list_of_slugs.remove(self.slug)
        print(self.list_of_slugs)
        return reverse('product_brand_url', kwargs={'slug': ''.join(self.list_of_slugs)})

    def clearBrands(self):
        self.list_of_slugs = []

    def __str__(self):
        return self.title

    # class All(object):
    #     list_of_slugs = []

