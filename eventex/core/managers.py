from django.db import models


class EmailContactManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(kind=self.model.EMAIL)
        return qs
