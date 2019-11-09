from django.db import models

# Create your models here.
class Gallery(models.Model):
    description = models.CharField(default="在这里写作品简介", max_length=200)
    FIELDONME = models.ImageField(default='default.png', upload_to='images/')
    title = models.CharField(default="production",max_length=50)

    def __str__(self):
        return self.title
