from django.db import models


class KindContactManager(models.Manager):
    def emails(self):
        return self.filter(kind=self.model.EMAIL)

    def phones(self):
        return self.filter(kind=self.model.PHONE)
