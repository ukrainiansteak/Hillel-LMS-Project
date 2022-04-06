from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(
        to='auth.User',
        on_delete=models.CASCADE,
        related_name="profile"
    )
    image = models.ImageField(
        null=True, blank=True,
        upload_to='pics/',
        validators=[
            FileExtensionValidator(['jpg', 'jpeg', 'png'])
        ])

    @classmethod
    def generate_profile(cls):
        for user in User.objects.all():
            try:
                user.profile
            except Profile.DoesNotExist:
                profile = Profile()
                profile.user = user
                profile.save()

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        if self.image:
            with Image.open(self.image) as im:
                if self.image.width > self.image.height:
                    width = 300
                    height = round(self.image.height * (width / self.image.width))
                elif self.image.width < self.image.height:
                    height = 300
                    width = round(self.image.width * (height / self.image.height))
                else:
                    width = 300
                    height = 300
                path = self.image.path
                self.image = im.resize((width, height), Image.ANTIALIAS)
                self.image.save(path)
