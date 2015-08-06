from django.shortcuts import render, get_object_or_404
from .models import urlSites
from bs4 import BeautifulSoup
import requests


def url_list(request):
    # source_code = requests.get(urlSites.objects.get)
    urlList = urlSites.objects.all().order_by('id')
    return render(request, 'archive/url_list.html', {'urlList': urlList})

def url_detail(request, pk):
    urlDetail = get_object_or_404(urlSites, pk=pk)
    return render(request, 'archive/url_detail.html', {'urlDetail': urlDetail})