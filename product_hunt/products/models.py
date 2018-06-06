from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    app_name = models.CharField(default='App name', max_length=50)
    description = models.TextField(default='App description')
    app_link = models.CharField(default='http://', max_length=50)
    app_icon = models.ImageField(default='default_icon.png', upload_to='image/')
    screen_shot = models.ImageField(default='default_screen_shot.png', upload_to='image/')
    
    votes = models.IntegerField(default=1)
    publish_date = models.DateField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.app_name

    def text_cut(self):
        if len(self.description) > 30:
            return self.description[:30] + '...'
        else:
            return self.description
