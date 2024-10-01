# webapp/middleware.py
from django.shortcuts import redirect

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is trying to access a protected view
        if request.path in ['/profile/', '/service_view/'] and 'username' not in request.session:
            return redirect('login_user')  # Redirect to your login page

        return self.get_response(request)
