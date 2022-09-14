from django.contrib import admin

from myapp1.models import Flower, Category

admin.site.register(Flower)
admin.site.register(Category)