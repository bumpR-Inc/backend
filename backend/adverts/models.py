from django.db import models

class Driver(models.Model):
	objects = models.Manager()

	profile = models.OneToOneField('accounts.Profile', on_delete=models.CASCADE)


# Create your models here.
class Org(models.Model):
	objects = models.Manager()

	profile = models.OneToOneField('accounts.Profile', on_delete=models.CASCADE)

	description = models.CharField(max_length=960, null=True)

class Advert(models.Model):
	objects = models.Manager()

    enabled = models.BooleanField(default=False)

	description = models.CharField(max_length=960, null=False, blank=False)

	org = models.ForeignKey(
		'Org',
		null=False,
		blank=False,
		on_delete=models.CASCADE,
	 	related_name="advert_org"
	)