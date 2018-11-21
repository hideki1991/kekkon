from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    datetime=models.DateTimeField(
            default=timezone.now)
    title=models.CharField(max_length=200)
    text=models.TextField()
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    category = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
    class Meta:
        ordering = ['-datetime']
