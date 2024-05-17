from django.contrib import admin

# Register your models here.
from .models import Museo, Autore, Opera
admin.site.register(Museo)
admin.site.register(Autore)
admin.site.register(Opera)