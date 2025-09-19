from django.contrib import admin

from .models import Bead

@admin.register(Bead)
class BeadAdmin(admin.ModelAdmin):
    list_display=('philosopher_name', 'text')
