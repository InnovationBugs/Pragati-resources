from django.db import models
import random
from datetime import date

# Create your models here.


def generateId():
    return random.randint(1,50)*3

class feedback(models.Model):
    msg_id = models.IntegerField(default=generateId(), primary_key=True, unique=True)
    email = models.TextField(unique=True)
    name = models.TextField(default="noname")
    subject = models.TextField(default="no topic")
    message = models.TextField(default="no message")
    date = models.DateTimeField(date.today())

    def __str__(self):
        return (self.msg_id+'\n'+self.date+'\n'+self.email+'\n'+self.subject+'\n'+self.name+'\n'+self.message+'\n')
