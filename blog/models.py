from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
# Create your models here.

class Blog(models.Model):
    datetime=models.DateTimeField(
            default=timezone.now)
    title=models.CharField(max_length=200)
    text=models.TextField()
    MY_CHOICES = (('コラム', 'コラム'),
              ('カスタム婚', 'カスタム婚'),
              ('item_key3', 'Item title 1.3'),
              ('item_key4', 'Item title 1.4'),
              ('item_key5', 'Item title 1.5'))
    document = models.FileField(upload_to='documents/blogs')
    category = MultiSelectField(choices=MY_CHOICES)
    class Meta:
        ordering = ['-datetime']
