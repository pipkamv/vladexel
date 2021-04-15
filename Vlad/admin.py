from django.contrib import admin
from .models import VladExelModels

class VladExelAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = VladExelModels
        field = '__all__'

admin.site.register(VladExelModels)
