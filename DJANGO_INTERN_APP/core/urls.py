from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),  
    path('public/', views.public_endpoint),
    path('protected/', views.protected_endpoint),
    path('login/', views.login_view),
    path('dashboard/', views.dashboard_view),
    path('test-task/', views.test_task),

]
