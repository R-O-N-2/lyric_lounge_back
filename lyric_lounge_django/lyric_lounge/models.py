from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField()
    location = models.CharField(max_length=100, default= 'location')
    contact = models.CharField(max_length=100, default= 'contact info')
    password = models.CharField(max_length=100, default='password')

    def __str__(self):
        return self.name



class Genre(models.Model):
    hip_hop = 'hip hop'
    pop = 'pop'
    rock = 'rock'
    metal = 'metal'
    other = 'other'
    
    genre_choices = [
        (hip_hop, 'hip hop'),
        (pop, 'pop'),
        (rock, 'rock'),
        (metal, 'metal'),
        (other, 'other')
    ]

    name = models.CharField(max_length=10, choices= genre_choices, default= hip_hop)
    
    def __str__(self):
        return self.name
    


class Work(models.Model):
   
    title = models.CharField(max_length=100)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genres', default= 1)

    def user_name(self):
        return self.user.name

    def __str__(self):
        return self.title
    
    def increment_likes(self):
        self.likes += 1
        self.save()
        
class Alias(models.Model):
    name = models.CharField(max_length=100)
    works = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='alias')