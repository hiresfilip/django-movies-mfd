from django.contrib import admin

# Import všech modelů, které obsahuje models.py
from.models import *

# Register your models here.
admin.site.register(Genre)
admin.site.register(Film)
admin.site.register(Attachment)