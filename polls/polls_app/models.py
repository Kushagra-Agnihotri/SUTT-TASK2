from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    publication_date =models.DateTimeField("publication date")
    def __str__(self):
        return self.question_text
    def was_pub_recently(self):
        return self.publication_date >= timezone.now() - datetime.timedelta(days=1)
    

class Choice(models.Model):
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    def __str__(self):
        return self.text
    
    
    
    