
import os

from django.db import models
from django.contrib.auth.models import User


def Report_Directory_Name(instance, filename):
    return os.path.join(
        "found_items/media/",
        instance.item_name,
        filename
    )


class ReportFoundItem(models.Model):

    TYPE_CHOICES = (
        ("Found", "Found"),
        ("Not Found", "Not Found"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="found_reports"
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

    date_found = models.DateField()

    location_found = models.CharField(max_length=100)

    contact_info = models.CharField(max_length=100)

    image = models.ImageField(
        upload_to=Report_Directory_Name,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.item_name

