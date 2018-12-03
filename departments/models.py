from django.db import models
from directions.models import Direction

# Create your models here.

class Department(models.Model):
    """Department model."""
    dep_description = models.CharField(max_length=140)
    fkdirection = models.ForeignKey(Direction, on_delete=models.CASCADE)

    def __str__(self):
        """"Return description"""
        return '{}'.format(self.dep_description)