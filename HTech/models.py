from django.db import models
from datetime import datetime
from django.core.mail import send_mail






#All status type
STATUS_CHOICES = (
    ('b', 'Banned'),
    ('f', 'Offline'),
    ('o', 'Online'),
)

STATUS_CHOICES_ONE = (
    ('r', 'Ready to Send'),
    ('d', 'Done'),
)

STATUS_CHOICES_TWO = (
    ('a', 'Active'),
    ('b', 'Banned'),
    ('i', 'Inactive')
)
# Create your models here.
class User(models.Model):
    FirstName = models.CharField(max_length=100, help_text="Enter the first name")
    LastName = models.CharField(max_length=100, help_text="Enter the last name")
    Country = models.CharField(max_length=100, help_text="Enter the country")
    PhoneNumber = models.IntegerField(help_text="Enter the phone number")
    Email = models.EmailField(max_length=100, help_text="Enter email address")
    Status = models.CharField(max_length=1, choices=STATUS_CHOICES_ONE)

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'All Users'


    def __str__(self):
        return "User %s, %s" % (self.Country, self.Email)





#Creating model for twilio
class Twillo(models.Model):
    AccountName = models.CharField(max_length=100, help_text="Enter Twilio Account Name")
    Phone = models.CharField(max_length=100, help_text="Enter the Account Phone Number")
    account_sid = models.CharField(max_length=100, help_text="Enter the Twilio SID")
    auth_token = models.IntegerField(help_text="Enter the Twillio Key")
    Email = models.EmailField(max_length=100, help_text="Enter email address")
    Status = models.CharField(max_length=1, choices=STATUS_CHOICES_TWO)

    class Meta:
        verbose_name = 'Twllo'
        verbose_name_plural = 'Twillo Accounts'

    def __str__(self):
        return "Twillo %s, %s" % (self.AccountName, self.Email)





#Creating model for server status parse
class ServerStatus(models.Model):
    ServerName = models.CharField(max_length=100, help_text="Enter the first name")
    Status = models.CharField(max_length=1, choices=STATUS_CHOICES)


    class Meta:
        verbose_name = 'Server Status'
        verbose_name_plural = 'Servers Status'

    def __str__(self):
        return "Twillo %s" % (self.ServerName)

#mail sender
