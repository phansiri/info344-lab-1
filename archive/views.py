from django.shortcuts import render, get_object_or_404, redirect
from .models import urlSites
from .forms import UrlForm
from bs4 import BeautifulSoup
import requests


def url_list(request):
    # source_code = requests.get(urlSites.objects.get)
    urlList = urlSites.objects.all().order_by('id')
    return render(request, 'archive/url_list.html', {'urlList': urlList})

def url_detail(request, pk):
    urlDetail = get_object_or_404(urlSites, pk=pk)
    if request.method == "POST":
        urlDetail.delete()
        # urlList = urlSites.objects.all().order_by('id')
        return redirect('archive.views.url_list')
    else:
        urlDetail = get_object_or_404(urlSites, pk=pk)
    return render(request, 'archive/url_detail.html', {'urlDetail': urlDetail})

def url_new(request):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            source_code = requests.request('GET', post.originalUrl)
            # source_code = requests.get(form)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, "html.parser")
            post.finalUrl = source_code.url
            post.httpStatusCode = source_code.status_code
            post.pageTitle = soup.title.string
            post.save()
            return redirect('archive.views.url_detail', pk=post.pk)
    else:
        form = UrlForm()
    return render(request, 'archive/url_edit.html', {'form': form})

def url_edit(request, pk):
    post = get_object_or_404(urlSites, pk=pk)
    if request.method == "POST":
        form = UrlForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('archive.views.url_detail', pk=post.pk)
    else:
        form = UrlForm(instance=post)
    return render(request, 'archive/url_edit.html', {'form': form})