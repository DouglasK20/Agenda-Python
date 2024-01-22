from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'show',
    ordering = 'id',
    # list_filter = 'created_date', --> Cria um filtro
    search_fields = 'id', 'first_name', 
    list_per_page = 10
    list_max_show_all = 50
    list_editable = 'show',
    list_display_links = 'id', 'first_name',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',