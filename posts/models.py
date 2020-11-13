from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    publishing_date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, upload_to='uploads')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
