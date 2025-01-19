from django.db import models

class Study(models.Model):
    name = models.CharField(max_length=100)
    phase = models.CharField(max_length=50)
    sponsor = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Subject(models.Model):
    study = models.ForeignKey(Study, related_name='subjects', on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.subject_name
