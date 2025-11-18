from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Thought(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(max_length=500)
    mood = models.CharField(max_length=20, choices=[
        ('😊', 'Happy'),
        ('😐', 'Neutral'),
        ('😔', 'Sad'),
        ('😤', 'Stressed'),
        ('🤩', 'Excited'),
    ])
    tag = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.date} - {self.mood}"
