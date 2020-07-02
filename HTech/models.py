from django.db import models
from datetime import datetime
from django.core.mail import send_mail


#All status type
STATUS_CHOICES_ONE = (
    ('r', 'Ready to Send'),
    ('d', 'Done'),
)


# Create your models here.
class User(models.Model):
    FirstName = models.CharField(max_length=100, help_text="Enter the first name")
    LastName = models.CharField(max_length=100, help_text="Enter the last name")
    Country = models.CharField(max_length=100, help_text="Enter the country")
    PhoneNumber = models.CharField(max_length=12,help_text="Enter the phone number")
    Email = models.EmailField(max_length=100, help_text="Enter email address")
    Status = models.CharField(max_length=1, choices=STATUS_CHOICES_ONE)

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'All Users'


    def __str__(self):
        return "User %s, %s" % (self.Country, self.Email)




