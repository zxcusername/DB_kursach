from django.db import models
from django.utils import timezone 

from django.contrib.auth.models import User

    # Create your models here.
class Dude(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #nickname = self.user.username 
    bio = models.TextField()
    photo = models.CharField(max_length=150) # путь до картинки
    is_judge = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Song(models.Model):
    author = models.ForeignKey(Dude, on_delete=models.CASCADE)      
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published', auto_now = True)
    lyrics = models.TextField()

    def __str__(self):
        return self.title

class Review(models.Model):
    author = models.ForeignKey(Dude, on_delete=models.PROTECT)     
    song = models.ForeignKey(Song, on_delete=models.CASCADE, default = None)  
    text_score = models.IntegerField(default=0)
    flow_score = models.IntegerField(default=0)
    general_score = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', auto_now = True)
    comment = models.TextField()

    def __str__(self):
        return self.author.user.username + ' про ' + self.song.author.user.username + ' – ' + self.song.title