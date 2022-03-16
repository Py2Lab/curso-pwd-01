from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    deadline = models.DateTimeField()
    project = models.ForeignKey()
    owner = models.ForeignKey()
    assignee = models.ForeignKey()

    def __str__(self):
        return self.title
