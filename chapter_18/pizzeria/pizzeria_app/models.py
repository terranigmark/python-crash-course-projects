from django.db import models

# Create your models here.
class Pizza(models.Model):
    """A pizza included in the restaurant menu"""
    name = models.CharField(max_length = 150)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name

class Description(models.Model):
    """Description of the pizzas"""
    description = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'descriptions'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."