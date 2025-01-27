from django.db import models

class PostData(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
