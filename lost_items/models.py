import os

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

def Report_Directory_Name(instance, filename):
    return os.path.join(
        "lost_items/media/",
        instance.item_name,
        filename
    )


class ReportLostItem(models.Model):

    TYPE_CHOICES = (
        ("Lost", "Lost"),
        ("Found", "Found"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="lost_reports",        
        null=True,
        blank=True
    )

    item_name = models.CharField(max_length=100)

    description = models.TextField()

    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES
    )

    category = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    date_lost = models.DateField()

    location_lost = models.CharField(max_length=100)

    contact_info = models.CharField(max_length=100)

    image = models.ImageField(
        upload_to=Report_Directory_Name,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.item_name