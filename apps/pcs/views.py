from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request): #show user login
    return render(request, 'pcs/index.html')
