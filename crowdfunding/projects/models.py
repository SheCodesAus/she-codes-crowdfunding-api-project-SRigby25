from django.contrib.auth import get_user_model
from django.db import models

DRINKS_HAD = (
    ('1drink', '1DRINK'),
    ('2drink', '2DRINK'),
    ('3drink', '3DRINK'),
    ('4drink', '4DRINK'),
    ('5+drink', '5+DRINK'),
)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    category = models.CharField(max_length=8, choices=DRINKS_HAD, default='1Drink')
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

