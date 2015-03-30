from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from apps.pcs.models import Page, Category, Item


def index(request): #show user login
    context = {
        'pages' : Page.objects.all().order_by('weight')
    }
    return render(request, 'pcs/index.html', context)
