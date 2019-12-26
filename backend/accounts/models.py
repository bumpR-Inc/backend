from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from adverts.models import *


# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Profile(models.Model):
    # The manager to get Profile objects
    objects = models.Manager()

    # the one to one relationship with the user, as the profile class builds off of django's built in user class
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # the main timezone for this user
    timezone = models.CharField(max_length=50, default='EST')

    # defines which type of member the user/profile belongs to
    CHOICES = (('1', 'Org',), ('2', 'Driver',))
    member_type = models.CharField(max_length=50, choices=CHOICES)

    def is_org(profile):
        return profile.member_type == '1'

    def is_driver(profile):
        return profile.member_type == '2'

    def get_profile_type(profile):
        if Profile.is_org(profile):
            return "Org"
        elif Profile.is_driver(profile):
            return "Driver"

    def get_org(profile):
        return Org.objects.filter(profile=profile).first()

    def get_driver(profile):
        return Driver.objects.filter(profile=profile).first()

    def name(profile):
        return profile.user.first_name + ' ' + profile.user.last_name

    def __str__(self):
        return self.user.username
