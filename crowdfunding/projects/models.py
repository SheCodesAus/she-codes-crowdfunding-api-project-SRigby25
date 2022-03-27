from django.contrib.auth import get_user_model
from django.db import models

DRINKS_HAD = (
    ('1 drink', '1 DRINK'),
    ('2 drink', '2 DRINK'),
    ('3 drink', '3 DRINK'),
    ('4 drink', '4 DRINK'),
    ('5+ drink', '5+ DRINK'),
)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    category = models.CharField(max_length=8, choices=DRINKS_HAD, default='1 Drink')
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='support_projects'
    )

