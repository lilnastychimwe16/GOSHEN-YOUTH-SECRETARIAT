from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class ZonalObligation(models.Model):
    CATEGORY_CHOICES = [
        ('chadzoka', 'Chadzoka (National Project)'),
        ('national_account', 'National Account'),
        ('zonal_seminar', 'Zonal Seminar'),
        ('nyc', 'National Youth Conference (NYC)'),
        ('weddings', 'Weddings'),
        ('provincial_project', 'Provincial Project'),
        ('zonal_admin', 'Zonal Admin'),
        ('national_donation', 'National Donation'),
        ('directors_gift', "Director's Gift"),
        ('hd', 'HD'),
        ('secretaries_seminar', 'Secretaries and Advisors Seminar'),
        ('advisors_conference', 'Advisors Conference'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)
    current_figure = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    projected_target = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['category']
        verbose_name = 'Zonal Obligation'
        verbose_name_plural = 'Zonal Obligations'

    def __str__(self):
        return f"{self.get_category_display()}: ${self.current_figure}"

    @property
    def balance(self):
        return self.projected_target - self.current_figure

    def clean(self):
        # Ensure only one record per category exists
        if not self.pk:  # Only check for new records
            if ZonalObligation.objects.filter(category=self.category).exists():
                raise ValidationError(f"An obligation for {self.get_category_display()} already exists.")

class DistrictObligation(models.Model):
    district_name = models.CharField(max_length=100, unique=True)
    current_figure = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    projected_target = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['district_name']
        verbose_name = 'District Obligation'
        verbose_name_plural = 'District Obligations'

    def __str__(self):
        return f"{self.district_name}: ${self.current_figure}"

    @property
    def balance(self):
        return self.projected_target - self.current_figure

    def clean(self):
        # Ensure only one record per district exists
        if not self.pk:  # Only check for new records
            if DistrictObligation.objects.filter(district_name=self.district_name).exists():
                raise ValidationError(f"An obligation for {self.district_name} already exists.")
