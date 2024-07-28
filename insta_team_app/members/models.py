from django.db import models
from django.utils import timezone

class Member(models.Model):
    ROLE_CHOICES = [
        ('r', 'Regular - Can\'t delete members'),
        ('a', 'Admin - Can delete members'),
    ]
    dateCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dateModified = models.DateTimeField(null=True, blank=True, default=timezone.now)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    emailId = models.CharField(null=True, blank=True, unique=True, max_length=100)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='r')
    imageUrl = models.CharField(max_length=200)
    isInActive = models.BooleanField(default=False)

    def __str__(self):
        return str(self.userId) + '| fname -' + str(self.first_name) + '| email -' + str(self.emailId)
    
# We can log activity for changes
class Logger(models.Model):
    dateCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dateModified = models.DateTimeField(null=True, blank=True, default=timezone.now)
    modifiedByModelName = models.CharField(blank=True, null=True, max_length=100)
    modifiedBymodelId = models.CharField(blank=True, null=True, max_length=10)
    modelName = models.CharField(blank=True, null=True, max_length=100)
    modelId = models.CharField(blank=True, null=True, max_length=10)
    fieldName = models.CharField(blank=True, null=True, max_length=100)
    fieldType = models.CharField(blank=True, null=True, max_length=100)
    oldValue = models.CharField(blank=True, null=True, max_length=200)
    newValue = models.CharField(blank=True, null=True, max_length=200)
    isInActive = models.BooleanField(default=False)

    def __str__(self):
        return str(self.modelName) + ",| model Id -" + str(self.modelId) + ",| updated field -" + str(self.fieldName) + " | updated value -" + str(self.newValue)