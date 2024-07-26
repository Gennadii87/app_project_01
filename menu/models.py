from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=500, blank=True, null=True)
    name_url = models.CharField(max_length=200, blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=200)

    def get_absolute_url(self):
        if self.name_url:
            return reverse(self.name_url)
        return self.url

    def __str__(self):
        return self.name
