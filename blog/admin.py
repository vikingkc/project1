from django.contrib import admin

from .models import *

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(BloodDonor)

# Register your models here.
