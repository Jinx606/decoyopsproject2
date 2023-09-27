from django.db import models

# Create your models here.
#I have the model for the contact form below and another class which will display messages in the admin page as opposed to being called contact
class Contact(models.Model):
    """Model representing a contact message.

    This model represents a message submitted via a contact form. It stores the name, surname, email address,
    and the message content.

    Attributes:
        name (CharField): The name of the person who submitted the message.
        surname (CharField): The surname of the person who submitted the message.
        email (EmailField): The email address of the person who submitted the message.
        message (TextField): The content of the message.

    Methods:
        __str__(): Returns the email address of the contact as a string.

    Meta:
        verbose_name (str): A human-readable name for the model in singular form.
        verbose_name_plural (str): A human-readable name for the model in plural form.
    """
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField(max_length=1200)
    

    def __str__(self):
        return self.email
        
        
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
