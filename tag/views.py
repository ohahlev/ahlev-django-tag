from django.shortcuts import render, get_list_or_404
from .models import Tag

def index(request):
    tags = get_list_or_404(Tag)
    context = {
        'tag': tags[0]
    }
    return render(request, 'tag/index.html', context=context)