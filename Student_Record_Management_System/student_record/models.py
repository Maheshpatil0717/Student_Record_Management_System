from django.db import models

# Create your models here.
class student(models.Model):
    Name = models.CharField(max_length=200)
    Roll = models.IntegerField()
    Marks = models.IntegerField()


    def _str_(self):
        return self.Name