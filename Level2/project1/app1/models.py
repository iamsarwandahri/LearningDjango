from django.db import models

class Topic(models.Model):
    topic_name = models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=264)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name
    

class AccessRecords(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date = models.DateField()
    def __str__(self):
        return self.name
    
