from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

def index(request):
    return redirect('Home')

def logout_view(request):
    logout(request)
    return redirect('index')

class AuthenticationView(TemplateView):
    template_name = "Main/Sign_in.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_signin_page'] = True  # Set the variable to True for the Sign In page
        return context

    def post(self, request, *args, **kwargs):
        username = request.POST['Username']
        password = request.POST['Password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        remember_me = request.POST.get('Remember_password')  # Check if Remember Me is selected

        # Set the session timeout based on Remember Me checkbox
        if remember_me:
            request.session.set_expiry(settings.SESSION_COOKIE_AGE)  # Set to a longer duration
        else:
            request.session.set_expiry(0)  # Use the session length

        if user is not None:
            login(request, user)  # Log in the user
            print("Authentication success")
            url = reverse('Home')
            return redirect(url)  # Redirect to a Home page
        
        else:
            # Authentication failed, show an error message
            print("Authentication failed")
            return render(request, self.template_name, {'error_message': 'Invalid credentials'})

@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = "Main/Home.html"


class AboutView(TemplateView):
    template_name = "Main/About.html"
