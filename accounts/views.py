from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import UserProfile
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('main_page'))  # Redirect to the desired page after successful login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(reverse('main_page'))

@login_required
def profile_view(request):
    profile = None  # Initialize profile variable with None

    if request.user.is_authenticated:
        try:
            profile = request.user.userprofile
        except UserProfile.DoesNotExist:
            # Handle the case when the user doesn't have a user profile
            # For example, you can create a new profile for the user
            profile = UserProfile(user=request.user)
            profile.save()
    else:
        pass
        # Handle the case when the user is not authenticated
        # For example, you can redirect them to the login page or display an error message
        # Add your desired logic here

    if request.method == 'POST':
        # Process the form data and update the profile
        # You can access the submitted data using request.POST['field_name']
        # Update the profile fields accordingly and save the changes
        # profile.save() <-- Remove this line

        messages.success(request, 'Profile updated successfully.')
        return redirect(reverse('profile'))

    return render(request, 'accounts/profile.html', {'profile': profile})


def my_orders_view(request):
    # Implement your my orders view logic here
    return render(request, 'accounts/my_orders.html')
