from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    industry = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"


class BusinessUnit(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='business_units')
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.company.name})"


class Metric(models.Model):
    CATEGORY_CHOICES = [
        ('environmental', 'Environmental'),
        ('social', 'Social'),
        ('governance', 'Governance'),
    ]

    business_unit = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE, related_name='metrics')
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    year = models.PositiveIntegerField()
    value = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.year}) - {self.category}"
