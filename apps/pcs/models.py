from django.db import models

# Create your models here.
class Page(models.Model):
    name        = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    weight      = models.IntegerField(max_length=11, default=0)
    created_at  = models.DateTimeField('Created', auto_now_add=True)
    updated_at  = models.DateTimeField('Modified', auto_now_add=True)
    def __str__(self):
        return "%s %s %s" % (self.name, self.description, self.weight)

class Category(models.Model):
    page        = models.ForeignKey(Page)
    name        = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    weight      = models.IntegerField(max_length=11, default=0)
    created_at  = models.DateTimeField('Created', auto_now_add=True)
    updated_at  = models.DateTimeField('Modified', auto_now_add=True)
    def __str__(self):
        return "%s %s %s %s" % (self.page, self.name, self.description, self.weight)

class Item(models.Model):
    category    = models.ForeignKey(Category)
    name        = models.CharField(max_length=100)
    description = models.TextField()
    price       = models.FloatField()
    weight      = models.IntegerField(max_length=11, default=0)
    created_at  = models.DateTimeField('Created', auto_now_add=True)
    updated_at  = models.DateTimeField('Modified', auto_now_add=True)
    def __str__(self):
        return "%s %s %s %s %s" % (self.Categories, self.name, self.description, self.price, self.weight)
