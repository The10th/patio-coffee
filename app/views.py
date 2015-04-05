from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from app.models import Page, Category, Item


def index(request): #show user login
    context = {
        'pages' : Page.objects.all().order_by('weight'),
        'categories' : Category.objects.all().order_by('Page').order_by('weight'),
        'items' : Item.objects.all().order_by('Category').order_by('weight')
    }
    return render(request, 'pcs/index.html', context)
