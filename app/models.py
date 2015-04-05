from django.db import models

# Create your models here.
class Page(models.Model):
    name        = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    weight      = models.IntegerField(max_length=11, default=0)
    created_at  = models.DateTimeField('Created', auto_now_add=True)
    updated_at  = models.DateTimeField('Modified', auto_now_add=True)
    def __str__(self):
        return "%s %s" % (self.weight, self.name)

class Category(models.Model):
    page        = models.ForeignKey(Page)
    name        = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    weight      = models.IntegerField(max_length=11, default=0)
    created_at  = models.DateTimeField('Created', auto_now_add=True)
    updated_at  = models.DateTimeField('Modified', auto_now_add=True)
    def __str__(self):
        return "%s %s %s" % (self.page, self.weight, self.name)

class Item(models.Model):
    category    = models.ForeignKey(Category)
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price       = models.FloatField()
    weight      = models.IntegerField(max_length=11, default=0)
    created_at  = models.DateTimeField('Created', auto_now_add=True)
    updated_at  = models.DateTimeField('Modified', auto_now_add=True)
    def __str__(self):
        return "%s %s %s %s" % (self.category, self.weight, self.name, self.price)
