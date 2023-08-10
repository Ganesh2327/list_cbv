from django.db import models

# Create your models here.
class trainer(models.Model):
    trainer_name=models.CharField(max_length=100, primary_key=True)
    sub=models.CharField(max_length=100)
    age=models.IntegerField()
    