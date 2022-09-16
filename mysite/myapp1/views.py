from django.shortcuts import render, get_object_or_404

from myapp1.models import Flower


def index(request):
    flowers = Flower.objects.all()

    return render(request, 'myapp1/index.html', {'flowers': flowers})


def detail(request, slug=None):
    flower = get_object_or_404(Flower, slug=slug)
    return render(request, 'myapp1/detail.html', {'flower': flower})


def tags(request, slug=None):
    flowers = Flower.objects.filter(tags__slug=slug)
    return render(request, 'myapp/index.html', {'flowers': flowers})
