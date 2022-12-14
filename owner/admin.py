from django.contrib import admin
from .models import  Owner
# Register your models here.
#admin.site.register(Owner)

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('nombre','edad','pais')
    search_fields = ('nombre',)
    list_filter = ('nombre',)
    fields = ('nombre',)