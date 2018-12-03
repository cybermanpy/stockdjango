from django.db import models
# Create your models here.


class Direction(models.Model):
    """Direction model. """
    dir_description = models.CharField(max_length=140)

    def __str__(self):
        """Return description"""
        return '{}'.format(self.dir_description)