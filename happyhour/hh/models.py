from django.db import models
from django.template.defaultfilters import slugify

import tagulous.models
from eventtools.models import BaseEvent, BaseOccurrence

# Create your models here.

class Bar(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField(blank=True)
    street_address = models.CharField(max_length=127)
    zipcode = models.IntegerField()
    city = models.CharField(max_length=63)
    phone = models.CharField(max_length=63, blank=True)
    website = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=5, blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, blank=True)

    def __str__(self):
        return self.name + ", " + self.city

class DrinkTags(tagulous.models.TagModel):
    class TagMeta:
        initial = 'beer, "long drink", cider, wine, \
        spirits, food, special, "sparkling wine", cocktails'
        force_lowercase = True

class HappyHour(BaseEvent):
    bar = models.ForeignKey(Bar, related_name='happyhours', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    drink_type = tagulous.models.TagField(to=DrinkTags)

    def __str__(self):
        return self.name

class HappyHourInstance(BaseOccurrence):
    event = models.ForeignKey(HappyHour, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s, %s-%s' % (self.event.bar, self.event.name, self.start.strftime('%a klo %H:%M'), self.end.strftime('%H:%M'))
