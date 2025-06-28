

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

@api_view(['GET'])
@permission_classes([AllowAny])
def public_endpoint(request):
    return Response({"message": "✅ This is a public endpoint accessible to anyone."})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_endpoint(request):
    return Response({"message": f"🔒 Hello, {request.user.username}! You accessed a protected endpoint."})

# Web-based login view
def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/dashboard/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# Simple dashboard
def dashboard_view(request):
    return render(request, 'dashboard.html', {'username': request.user.username})

from django.http import HttpResponse

def home(request):
    return HttpResponse("🎉 Welcome to the Django Intern App! Go to /api/public or /login")
from .tasks import send_welcome_email

@api_view(['GET'])
@permission_classes([AllowAny])
def test_task(request):
    send_welcome_email.delay("TestUser")
    return Response({"status": "Task triggered!"})
