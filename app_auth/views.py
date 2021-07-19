from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
def home_page(request):
    context = {
        'app_name' : 'Nadha-Education-Data-Control'
    }
    return render(request, 'auth/home-page.html', context)

def login_page(request):
    context = {
        'app_name' : 'Nadha-Education-Data-Control'
    }
    return render(request, 'auth/login-page.html', context)