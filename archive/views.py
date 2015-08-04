from django.shortcuts import render

def url_list(request):
    return render(request, 'archive/url_list.html', {})