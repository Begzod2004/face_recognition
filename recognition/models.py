from django.db import models

class UserImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='user_images/')

    def __str__(self):
        return self.name