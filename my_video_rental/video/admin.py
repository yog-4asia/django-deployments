from django.contrib import admin
from . import models

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    fields = ['last_name','first_name','phone']
    search_fields = ['first_name', 'last_name']

class MovieAdmin(admin.ModelAdmin):
    search_fields = ['title','release_year','length']

    list_filter = ['release_year','length']

    list_display = ['title','release_year','length']

    list_editable = ['length']

admin.site.register(models.Movie,MovieAdmin)
admin.site.register(models.Customer,CustomerAdmin)
