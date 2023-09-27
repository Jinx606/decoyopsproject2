from django.db import models

# Create your models here.
#I have the model for the contact form below and another class which will display messages in the admin page as opposed to being called contact
class Contact(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField(max_length=1200)
    

    def __str__(self):
        return self.email
        
        
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
