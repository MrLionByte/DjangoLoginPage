from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache
from django.contrib import messages,auth

# check weather user is already authenticated,if not Login page is loaded
@never_cache
def indexLogin(request):
    if request.user.is_authenticated:
        return redirect("homepage")
    else:
        return render(request,"index.html")
   
# Function to check weather user credentials are right or wrong.if authenticated redirect to homepage function,else if wrong redirected to login page 
def perform_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_object = auth.authenticate(request, username=username, password=password)
        if user_object is not None:
            auth.login(request, user_object)
            return redirect('homepage')
        else:
            messages.error(request,"User name or password is incorrect")
            return redirect("indexLogin")
    else:
         return redirect("indexLogin")

 # home page is loaded if user is authenticated and also make sure it doesn't cache 
@never_cache
def homepage(request):
    if request.user.is_authenticated:
        return render(request,"admin_dashboard.html")
    return redirect("indexLogin")

#logout button ,if user logged out the session will be cleared and returned to login page
def perform_logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request,"Logout Successful")
        return redirect("indexLogin")
    
def page(request):
    return render(request,"page.html")

###########
