from django.contrib import admin
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(NeighbourHood)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(Contact)


