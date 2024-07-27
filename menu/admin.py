from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(admin.StackedInline):  # для горизонтального расположения можно использовать TabularInline
    model = MenuItem
    extra = 1
    fields = ('menu_item_title', 'url', 'named_url', 'parent')


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [MenuItemInline]


admin.site.register(Menu, MenuAdmin)
