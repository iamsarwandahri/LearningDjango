from django.db import models

class Student(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=264)
    
    def __str__(self):
        return self.fname
