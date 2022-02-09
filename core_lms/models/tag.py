from django.db import models


class Tag(models.Model):
    name = models.SlugField(max_length=20)

    def __str__(self):
        return f'Tag {self.id} {self.name}'
