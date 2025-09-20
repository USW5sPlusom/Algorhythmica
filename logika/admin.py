from django.contrib import admin

from .models import Bead

@admin.register(Bead)
class BeadAdmin(admin.ModelAdmin):
    list_display=('philosopher_name', 'short_text')
    search_fields = ('philosopher_name', 'text')

    def short_text(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    short_text.short_description = 'Текст (кратко)'
