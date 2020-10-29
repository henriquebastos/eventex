from django.db import models


class Speaker(models.Model):
    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('slug')
    photo = models.URLField('foto')
    website = models.URLField('website')
    description = models.TextField('descrição')

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'