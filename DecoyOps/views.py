from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Contact
from django.db import models
from django.urls import reverse
from django.contrib import messages


# This view is for the info page and requires the render import from Django which will return the rendered info page
def info_view(request):
    """Render the 'info' page.

    This view checks if the user is authenticated. If authenticated, it renders the 'DecoyOps/info.html' template.
    If not authenticated, it redirects the user to the login page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered 'DecoyOps/info.html' or redirection to the login page.
    """
    if request.user.is_authenticated:
        return render(request, 'DecoyOps/info.html')
    else:
        return redirect('DecoyOps:login')


# This view is for the work page and requires the render import from Django which will return the rendered work page
def work_view(request):
    """Render the 'work' page.

    This view checks if the user is authenticated. If authenticated, it renders the 'DecoyOps/work.html' template.
    If not authenticated, it redirects the user to the login page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered 'DecoyOps/work.html' or redirection to the login page.
    """
    if request.user.is_authenticated:
        return render(request, 'DecoyOps/work.html')
    else:
        return redirect('DecoyOps:login')
    
    
# This view is for the superskin page which can only be accessed through the work page or previous button and requires the render import from Django which will return the rendered superskin page
def SUPERSKIN_view(request):
    """Render the 'SUPERSKIN' page.

    This view renders the 'DecoyOps/SUPERSKIN.html' template.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered 'DecoyOps/SUPERSKIN.html'.
    """
    return render(request, 'DecoyOps/SUPERSKIN.html')
    

# This view is for the unnatural page which can only be accessed through the work page or next button and requires the render import from Django which will return the rendered unnatural page
def UNNATURAL_view(request):
    """Render the 'UNNATURAL' page.

    This view renders the 'DecoyOps/UNNATURAL.html' template.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered 'DecoyOps/UNNATURAL.html'.
    """
    return render(request, 'DecoyOps/UNNATURAL.html')
    
    
# This view is for the Adidas page which can only be accessed through the work page or next button and requires the render import from Django which will return the rendered Adidas page
def ADIDAS_view(request):
    """Render the 'ADIDAS' page.

    This view renders the 'DecoyOps/ADIDAS.html' template.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered 'DecoyOps/ADIDAS.html'.
    """
    return render(request, 'DecoyOps/ADIDAS.html')
    
    
# This view is for the textiles page which can only be accessed through the work page or next button and requires the render import from Django which will return the rendered textiles page
def TEXTILES_view(request):
    """Render the 'TEXTILES' page.

    This view renders the 'DecoyOps/TEXTILES.html' template.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered 'DecoyOps/TEXTILES.html'.
    """
    return render(request, 'DecoyOps/TEXTILES.html')


# This view is for the contact page and it has a model class as well as a form in forms.py. if succesful submission has occurred the message will be logged in the admin page and a success message will appear on the screen.
def contact(request):
    """Handle form submission for the 'contact' page.

    This view handles POST requests for the 'contact' page. It saves contact form data to the database and
    displays a success message. If the request method is GET, it renders the 'DecoyOps/contact.html' template.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered 'DecoyOps/contact.html' (GET) or redirection to the 'contact' page (POST).
    """
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        message = request.POST['message']
        data = Contact(name=name,surname=surname, email=email, message=message)
        data.save()
        
        messages.success(request, 'Message submitted successfully!')

        contact_url = reverse('DecoyOps:contact')
        return redirect(contact_url)
    else:
        return render(request, 'DecoyOps/contact.html')


# This view is for registration and if the registration is successful, the navbar will become active and you will be directed to the info page
def user_registration(request):
    """Handle user registration.

    This view handles user registration using the 'RegistrationForm'. If registration is successful, it logs the
    user in and redirects to the 'info' page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered 'DecoyOps/register.html' (GET) or redirection to the 'info' page (POST).
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('DecoyOps:info')
    else:
        form = RegistrationForm()
    return render(request, 'DecoyOps/register.html', {'form': form})
    

# This view is for login and if the login is successful, the navbar will become active and you will be directed to the info page
def user_login(request):
    """Handle user login.

    This view handles user login using the 'AuthenticationForm'. If login is successful, it logs the user in and
    redirects to the 'info' page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered 'DecoyOps/login.html' (GET) or redirection to the 'info' page (POST).
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('DecoyOps:info')
    else:
        form = AuthenticationForm()
    return render(request, 'DecoyOps/login.html', {'form': form})


# Once succesfully logged in, this view for logging out will allow for a logout function which returns you to the login page
def user_logout(request):
    """Handle user logout.

    This view logs the user out and redirects to the login page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Redirection to the login page.
    """
    logout(request)
    return redirect('DecoyOps:login')

