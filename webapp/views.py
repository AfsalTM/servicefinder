from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from webapp.models import signindb,Service


# Create your views here.
# Home page
def home_page(request):
    if 'username' in request.session:  # Check if user is logged in via session
        search_query = request.GET.get('search')  # Get the search query from the request
        if search_query:
            services = Service.objects.filter(job__icontains=search_query)  # Filter services based on the query
        else:
            services = Service.objects.all()

        return render(request, 'home.html', {'services': services, 'username': request.session['username']})  # Pass the session username

    else:
        return redirect(login_user)  # If not logged in, redirect to login page



def login_user(request):
    return render(request,'login_page.html')
def sign_user(request):
    return render(request,'sign_in.html')


def save_user(request):
    if request.method=="POST":
        a = request.POST.get('username')
        b = request.POST.get('email')
        c = request.POST.get('p1')
        if signindb.objects.filter(email=b).exists():

            messages.error(request, "Email is already registered. Please use a different email.")
            return redirect(sign_user)

        obj=signindb(username=a,email=b,password=c)
        obj.save()
        return redirect(login_user)


def user_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')

        # Check if user exists with the provided username and password
        user = signindb.objects.filter(username=un, password=pwd).first()

        if user:  # If user is found
            request.session['username'] = un  # Store username in session
            return redirect(home_page)  # Redirect to home page after successful login
        else:
            messages.error(request, "Invalid username or password.")  # Show error message
            return redirect(login_user)  # Redirect back to login page for retry
    else:
        # If not a POST request, just render the login page
        return render(login_user)


 # Ensure the user is logged in
def profile_page(request):
    if 'username' in request.session:  # Check if user is logged in
        current_user = signindb.objects.get(username=request.session['username'])
    # Get the user's services based on the signindb model
        user_services = Service.objects.filter(user=current_user)   # Correct association
        return render(request, 'profile.html', {'services': user_services})



def service_view(request):
    if 'username' in request.session:  # Check if user is logged in
        if request.method == 'POST':
            name = request.POST.get('name')
            job = request.POST.get('job')
            price = request.POST.get('price')

            current_user = signindb.objects.get(username=request.session['username'])  # Fetch the current user
            obj = Service(user=current_user, name=name, job=job, price=price)
            obj.save()

            messages.success(request, "Service created successfully!")
            return redirect(profile_page)
    else:
        return redirect(login_user)  # Redirect to login if not logged in

def profile_view(request):
    if 'username' in request.session:  # Check if user is logged in
        current_user = signindb.objects.get(username=request.session['username'])  # Fetch the logged-in user
        user_services = Service.objects.filter(user=current_user)  # Get services posted by the user
        return render(request, 'profile.html', {'services': user_services})


def logout_user(request):
    if 'username' in request.session:
        del request.session['username']  # Remove the username from session
        messages.success(request, "You have been logged out successfully.")
    return redirect(login_user)  # Redirect to login page after logout





