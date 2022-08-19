from distutils.command.upload import upload
from tkinter import CASCADE
from tkinter.tix import IMAGE
from django.db import models
from django.contrib.auth import get_user_model
from tinymce import models as tinymce_models


# Create your models here.

User = get_user_model()

class Trainers(models.Model):
    Name= models.OneToOneField(User, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='pics')
    Position = models.CharField(max_length=70)

    def __str__(self):
        return str(self.Name)


class Hero(models.Model):
    Title = models.CharField(max_length=70)
    Description= tinymce_models.HTMLField(null=True)

    def __str__(self):
        return str(self.Title)

class Benefits(models.Model):
    Title = models.CharField(max_length=70)
    Description= tinymce_models.HTMLField(null=True)
    Image = models.ImageField(upload_to='pics')

    def __str__(self):
        return str(self.Title)

class History(models.Model):
    Title = models.CharField(max_length=70)
    Description= tinymce_models.HTMLField(null=True)
    Subtitle1 = models.CharField(max_length=70)
    Subdescr = tinymce_models.HTMLField(null=True)
    Subtitle2 = models.CharField(max_length=70)
    Subdescr2 = tinymce_models.HTMLField(null=True)
    Image = models.ImageField(upload_to='pics')

    def __str__(self):
        return str(self.Title)

class Step(models.Model):
    Title = models.CharField(max_length=70)
    Description = tinymce_models.HTMLField(null=True)
    

    def __str__(self):
        return str(self.Title)

class Testimonial(models.Model):
    Title = models.CharField(max_length=70)
    Description = tinymce_models.HTMLField(null=True)
    

    def __str__(self):
        return str(self.Title)

class Members(models.Model):
    Name = models.CharField(max_length=70)
    Workout = models.CharField(max_length=70)
    Description = tinymce_models.HTMLField(null=True)

    def __str__(self):
        return str(self.Name)

class Timetable(models.Model):
    Day = models.CharField(max_length=10)
    Time = models.TimeField
    Exercise = models.BooleanField

    


