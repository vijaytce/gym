from django.db import models

# Create your models here.
class userdata (models.Model):
        name = models.CharField(max_length=200)
        age = models.BigIntegerField()
        weight= models.BigIntegerField()
        height=models.BigIntegerField()
        bmi = models.FloatField()
        
        
        
        
        def __str__(self):
            return self.name
        
        
        