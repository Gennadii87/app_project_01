from django.db import models


class Menu(models.Model):
    objects = None
    name = models.CharField(max_length=100, unique=True, verbose_name='название меню')

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    objects = None
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE, verbose_name='меню')
    parent = models.ForeignKey(
                            'self',
                            null=True,
                            blank=True,
                            related_name='children',
                            on_delete=models.CASCADE,
                            verbose_name='наследовать'
                        )
    menu_item_title = models.CharField(max_length=100, verbose_name='название объекта меню')
    url = models.CharField(max_length=200, blank=True, null=True, verbose_name='url объекта меню')
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='заголовок')

    def get_url(self):
        if self.url:
            return self.url
        return '#'

    def __str__(self):
        return self.menu_item_title
