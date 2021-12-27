from django.db import models
from django.contrib.auth.models import User
import datetime
from time import time

from django.db.models.signals import post_save , pre_delete , pre_save , post_delete
from django.contrib.postgres.fields import ArrayField,HStoreField

# Create your models here.
colors = (
    ('Red','Red'),
    ('Yellow','Yellow'),
    ('Pink','Pink'),
    ('Grey','Grey'),
    ('Peach', 'Peach'),
    ('Black', 'Black'),
    ('White', 'White'),
)
