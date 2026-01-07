from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    user = request.user

    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            user.email = email
            user.save()

    return render(request, "accounts/profile.html", {"user": user})