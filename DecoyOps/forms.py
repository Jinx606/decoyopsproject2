from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Import the User model


class RegistrationForm(UserCreationForm):
    """Form for user registration.

    This form is based on the UserCreationForm provided by Django's authentication framework.
    It includes fields for username, email, and password (with password confirmation).

    Attributes:
        model (User): The User model to use for registration.
        fields (list): A list of fields to include in the form.
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
