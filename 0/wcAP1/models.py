from django.db import models

# Create your models here.

class WCUser(models.Model):
	name = models.CharField(max_length=255)
	fakeID = models.CharField(max_length=255)
	crptID = models.CharField(max_length=255)
	msgCount = models.IntegerField()
	realName = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class WCMsg(models.Model):
	msgID =models.CharField(max_length=255)
	msgTimestamp = models.CharField(max_length=255)
	msgCrptID = models.CharField(max_length=255)
	msgFakeID = models.CharField(max_length=255)
	msgFrom = models.ForeignKey(WCUser)
	msgContent = models.CharField(max_length=5000)
