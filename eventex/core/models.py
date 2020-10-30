from django.db import models
from django.shortcuts import resolve_url as r


class Speaker(models.Model):
    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('slug')
    photo = models.URLField('foto')
    website = models.URLField('website', blank=True)
    description = models.TextField('descrição', blank=True)

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)


class Contact(models.Model):
    KINDS =(
        ('E', 'Email'),
        ('P', 'Telefone'),
    )
    speaker = models.ForeignKey('Speaker', on_delete=models.CASCADE)
    kind = models.CharField(max_length=1, choices=KINDS)
    value = models.CharField(max_length=255)