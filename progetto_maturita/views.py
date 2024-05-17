from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.
class MyLoginView(LoginView):
    def get_success_url(self):
        return reverse_lazy('homepage')  # Reindirizza alla homepage dopo il login

def index_root(request):
    return render(request, "index_root.html")
