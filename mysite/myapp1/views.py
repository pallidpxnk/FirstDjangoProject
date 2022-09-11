from django.shortcuts import render

from myapp1.models import Flower


def index(request):
    flowers = Flower.objects.all()

    return render(request, 'myapp1/index.html', {'flowers': flowers})
