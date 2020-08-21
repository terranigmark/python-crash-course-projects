from django.db import models

# Create your models here.
class Pizza(models.Model):
    """A pizza included in the restaurant menu"""
    name = models.CharField(max_length = 150)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name