from django.contrib import admin

# Register your models here.
from .models import Adie, Company, Offer

admin.site.register(Adie)
admin.site.register(Company)
admin.site.register(Offer)
