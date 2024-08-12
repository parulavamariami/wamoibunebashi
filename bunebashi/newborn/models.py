from django.db import models
from django.contrib.auth.models import AbstractUser

class Username(models.Model):
    fullname = models.CharField(max_length=300)
    contact = models.IntegerField()
    about = models.TextField()

    def __str__(self):
        return self.fullname

class Genre(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

class Service(models.Model):
    creator = models.ForeignKey('User', on_delete=models.SET("Unknown Creator"))
    picture = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre, related_name='services', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    username = models.ForeignKey(Username, on_delete=models.SET('404! USER NOT FOUND!'))
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created', 'price']

    def __str__(self):
        return f'{self.title} by {self.username}'

class User(AbstractUser):
    services = models.ManyToManyField(Service, related_name='users', blank=True)
    avatar = models.ImageField(null=True, default='avatar.png')
    bio = models.TextField(null=True)

class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.body
