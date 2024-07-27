from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse, NoReverseMatch


class Menu(models.Model):
    objects = None
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    objects = None
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    menu_item_title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True, null=True)
    named_url = models.CharField(max_length=100, blank=True, null=True)

    def get_url(self):
        if self.url:
            return self.url
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                print(f"NoReverseMatch: '{self.named_url}' is not a valid view function or pattern name.")
                return '#'
        return '#'

    # def clean(self):
    #     # Проверка на циклические ссылки
    #     if self.parent and self.parent == self:
    #         raise ValidationError("An item cannot be its own parent.")
    #
    #     # Проверка на циклические ссылки в иерархии
    #     if self.parent and self.parent in self.get_ancestors():
    #         raise ValidationError("This parent item creates a cycle in the menu hierarchy.")
    #
    # def get_ancestors(self):
    #     ancestors = []
    #     parent = self.parent
    #     while parent:
    #         ancestors.append(parent)
    #         parent = parent.parent
    #     return ancestors

    def __str__(self):
        return self.menu_item_title
