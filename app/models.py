from django.db import models

# Create your models here.
class Page(models.Model):
    name        = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    weight      = models.IntegerField(default=0)
    endMessage  = models.TextField(blank=True, default='')
    created_at  = models.DateTimeField('Created', auto_now_add=True)
    updated_at  = models.DateTimeField('Modified', auto_now_add=True)
    def __str__(self):
        return "%s %s" % (self.weight, self.name)

class Category(models.Model):
    page        = models.ForeignKey(Page)
    name        = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    weight      = models.IntegerField(default=0)
    endMessage  = models.TextField(blank=True, default='')
    showHeading = models.BooleanField(default=False)
    heading1    = models.CharField(max_length=10, blank=True)
    heading2    = models.CharField(max_length=10, blank=True)
    created_at  = models.DateTimeField('Created', auto_now_add=True)
    updated_at  = models.DateTimeField('Modified', auto_now_add=True)
    def __str__(self):
        return "%s %s %s" % (self.page, self.weight, self.name)

class Item(models.Model):
    category    = models.ForeignKey(Category)
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price1      = models.FloatField(blank=True, default=0.00)
    price2      = models.FloatField(blank=True, default=0.00)
    weight      = models.IntegerField(default=0)
    isVegan     = models.BooleanField(default=False)
    isVegtarian = models.BooleanField(default=False)
    created_at  = models.DateTimeField('Created', auto_now_add=True)
    updated_at  = models.DateTimeField('Modified', auto_now_add=True)
    def __str__(self):
        return "%s %s %s" % (self.category, self.weight, self.name)
