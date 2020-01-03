from django.db import models

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    name = models.CharField(max_length = 255, blank=True, null = True)

    def __str__(self):
        return self.file.name

    #Please note that the files uploaded to FileField or ImageField are not saved in the database but in the file system of
    #your server. In the database it's the fields are represented by a VARCHAR containing the reference to the file.
    #It's mandatory to MEDIA_URL and MEDIA_ROOT in your settings file.