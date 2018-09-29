from django.contrib import admin

# Register your models here.
from .models import Paper, LifeGdp

admin.site.register(Paper)
admin.site.register(LifeGdp)
