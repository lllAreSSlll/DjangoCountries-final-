from django.db import models


class Language(models.Model):
    language = models.CharField(max_length=256,)

    def __str__(self):
        return self.language


class Country(models.Model):
    name = models.CharField(max_length=256)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name
