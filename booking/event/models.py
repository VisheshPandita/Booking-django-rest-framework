from django.db import models
import uuid
from user.models import Profile


class Event(models.Model):

    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    host = models.ForeignKey(
        Profile,
        related_name="host",
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='Event Name',
        max_length=200
    )
    seats = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    audience = models.ManyToManyField(
        Profile,
        related_name="audience"
    )
    discription = models.TextField(
        verbose_name='About the event',
        null=True,
        blank=True
    )
    time_start = models.DateTimeField(verbose_name='Time of starting of event')
    time_end = models.DateTimeField(verbose_name='Time of ending of event')
    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
    )
    address2 = models.CharField(
        "Address line 2",
        max_length=1024,
        null=True,
        blank=True
    )
    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
    )
    city = models.CharField(
        "City",
        max_length=1024,
    )
    country = models.CharField(
        "Country",
        max_length=3,
    )

    def __str__(self):
        return self.name