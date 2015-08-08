# Lab 1 - imports
from django.shortcuts import render, get_object_or_404, redirect
from .models import urlSites
from .forms import UrlForm
from bs4 import BeautifulSoup
import requests

# Lab 2 - imports
from django.contrib.auth.decorators import login_required



# Lab 1 - url expander
@login_required
def url_list(request):
    urlList = urlSites.objects.all().order_by('id')
    return render(request, 'archive/url_list.html', {'urlList': urlList})

@login_required
def url_detail(request, pk):
    urlDetail = get_object_or_404(urlSites, pk=pk)
    return render(request, 'archive/url_detail.html', {'urlDetail': urlDetail})

@login_required
def url_new(request):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            source_code = requests.request('GET', post.originalUrl)
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

@login_required
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

@login_required
def url_delete(request, pk):
    urlDelete = get_object_or_404(urlSites, pk=pk)
    urlDelete.delete()
    return redirect('archive.views.url_list')

# Lab 2 - Wayback API and Authentication

