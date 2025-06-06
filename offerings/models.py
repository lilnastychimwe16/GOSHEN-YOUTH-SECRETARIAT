from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FreewillOffering(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    week_start_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-week_start_date']
        verbose_name = 'Freewill Offering'
        verbose_name_plural = 'Freewill Offerings'

    def __str__(self):
        return f"Offering for week of {self.week_start_date}: ${self.amount}"
