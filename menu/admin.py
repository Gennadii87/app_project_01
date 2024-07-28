from django.contrib import admin
from django import forms
from .models import Menu, MenuItem


class MenuItemInlineForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            # Исключаем текущий объект из списка родительских элементов
            self.fields['parent'].queryset = MenuItem.objects.exclude(id=self.instance.id)


class MenuItemInline(admin.StackedInline):  # Можно использовать TabularInline для табличного отображения
    model = MenuItem
    form = MenuItemInlineForm
    extra = 1
    fields = ('menu_item_title', 'url', 'title', 'parent')


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [MenuItemInline]


admin.site.register(Menu, MenuAdmin)
